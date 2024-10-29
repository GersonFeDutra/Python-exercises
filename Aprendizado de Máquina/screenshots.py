#!/usr/bin/python3
'''
Take screenshots from a youtube video, in fixed intervals.
'''
import os
import re
import sys
import subprocess
import yt_dlp


def log(message: str, *args, **kwargs) -> None:
    GREEN: str = '\33[32m'
    RESET: str = '\33[m'
    _file=sys.stderr
    if 'file' in kwargs:
        file=kwargs['file']
    print(f'{GREEN}{message}{RESET}', *args, file=sys.stderr, **kwargs)


def warn(message: str, *args, **kwargs) -> None:
    YELLOW: str = '\33[33m'
    RESET: str = '\33[m'
    print(f'{YELLOW}{message}{RESET}', *args, file=sys.stderr, **kwargs)


def err(message: str, *args, **kwargs) -> None:
    RED: str = '\33[31m'
    RESET: str = '\33[m'
    print(f'{RED}{message}{RESET}', *args, file=sys.stderr, **kwargs)


def is_valid_youtube_url(url):
    # Expressão regular para verificar a URL do YouTube
    youtube_pattern = re.compile(
        r'^(https?://)?(www\.)?'
        r'(youtube\.com/|youtu\.be/)',  # URL normal ou shortened
        #r'([a-zA-Z0-9_-]{11})$',  # ID do vídeo
        re.IGNORECASE
    )
    return re.match(youtube_pattern, url) is not None


def is_valid_url(url):
    url_pattern = re.compile(
        r'^(https?://)?'  # Esquema (opcional)
        r'(\w+\.)?'       # Subdomínio (opcional)
        r'[a-zA-Z0-9.-]+' # Domínio
        r'\.[a-zA-Z]{2,}' # Sufixo de domínio
        r'(/.*)?$',       # Caminho (opcional)
        re.IGNORECASE
    )
    return re.match(url_pattern, url) is not None


from enum import Enum


class YT_URL_TYPE(Enum):
    UNKNOWN=0
    VIDEO=1
    PLAYLIST=2
    VIDEO_IN_PLAYLIST=3


def identify_youtube_url_type(youtube_url: str) -> YT_URL_TYPE:
    '''
    Identifica se a URL corresponde a um vídeo, playlist ou vídeo em playlist usando expressões regulares.
    Retorna 'video' se for um vídeo, 'playlist' se for uma playlist, ou 'video_in_playlist' se for um vídeo em playlist.
    '''
    # Expressão regular para uma URL de vídeo
    video_pattern = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/(watch\?v=|embed/|v/|.+\?v=)([a-zA-Z0-9_-]{11})"
    
    # Expressão regular para uma URL de playlist
    playlist_pattern = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/playlist\?list=([a-zA-Z0-9_-]+)"
    
    # Expressão regular para um vídeo em playlist
    video_in_playlist_pattern = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/watch\?v=([a-zA-Z0-9_-]{11})&list=([a-zA-Z0-9_-]+)"
    
    # Verifica cada padrão na URL
    if re.match(video_in_playlist_pattern, youtube_url):
        return YT_URL_TYPE.VIDEO_IN_PLAYLIST
    elif re.match(video_pattern, youtube_url):
        return YT_URL_TYPE.VIDEO
    elif re.match(playlist_pattern, youtube_url):
        return YT_URL_TYPE.PLAYLIST
    else:
        return YT_URL_TYPE.UNKNOWN


class Timestamp():
    _seconds: float
    _timestamp: str

    # Função para converter segundos em formato de timestamp (dd hh:mm:ss)
    @staticmethod
    def seconds_to_timestamp(s: float) -> str:
        seconds = int(s)
        #days: int = seconds // (24 * 60 * 60)  # Calcula o número de dias
        #hours: int = (seconds % (24 * 60 * 60)) // (60 * 60) # Total de horas (truncado)

        hours: int = seconds // (60 * 60) # Total de horas (truncado)
        minutes: int = (seconds % (60 * 60)) // 60 # Resto em min
        milliseconds: float = (s - seconds) % 60 * 1000 # Resto em ms
        seconds %= 60  # Restante em segundos

        # Formato dd hh:mm:ss.ms
        #return f'{days} {hours:02}:{minutes:02}:{seconds:02}.{milliseconds:04.0f}'
        # Formato hh:mm:ss.ms
        return f'{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:04.0f}'
        #return f'{hours:02}:{minutes:02}:{seconds:02}'


    # Função para converter timestamp (dd hh:mm:ss) em segundos
    @staticmethod
    def timestamp_to_seconds(timestamp):
        parts = timestamp.split()
        
        # Check if there's a day part
        if len(parts) == 2:
            days = int(parts[0])
            time_part = parts[1]
        else:
            days = 0
            time_part = parts[0]
        
        # Split hours, minutes, seconds
        hours, minutes, seconds = map(int, time_part.split(':'))
        
        # Convert to total seconds
        total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds
        return total_seconds


    @property
    def seconds(self) -> float:
        """The seconds property."""
        return self._seconds
    @seconds.setter
    def seconds(self, value: float) -> None:
        self._seconds = value
        self._timestamp = Timestamp.seconds_to_timestamp(value)
    @property
    def timestamp(self) -> str:
        """The timestamp property."""
        return self._timestamp
    @timestamp.setter
    def timestamp(self, value: str) -> None:
        self._timestamp = value
        self._seconds = Timestamp.timestamp_to_seconds(value)

    def as_file_name(self) -> None:
        return self._timestamp.replace(':', '-')

    def __str__(self) -> str:
        return self._timestamp

    def __add__(self, o):
        if isinstance(o, int) or isinstance(o, float):
            return Timestamp(self._seconds + o)
        elif isinstance(o, Timestamp):
            return Timestamp(self._seconds + o.seconds)
        else:
            raise TypeError

    def __lt__(self, o):
        if isinstance(o, Timestamp):
            return self._seconds < o._seconds
        elif isinstance(o, (float, int)):
            return self._seconds < o
        else:
            raise TypeError("Unsupported comparison type")

    def __eq__(self, o):
        if isinstance(o, Timestamp):
            return self._seconds == o._seconds
        elif isinstance(o, (float, int)):
            return self._seconds == o
        else:
            raise TypeError("Unsupported comparison type")

    def __ne__(self, o) -> bool:
        if isinstance(o, Timestamp):
            return self._seconds == o._seconds
        elif isinstance(o, (float, int)):
            return self._seconds == o
        else:
            raise TypeError("Unsupported comparison type")

    def __le__(self, o):
        if isinstance(o, Timestamp):
            return self._seconds <= o._seconds
        elif isinstance(o, (float, int)):
            return self._seconds <= o
        else:
            raise TypeError("Unsupported comparison type")

    def __init__(self, time: int | float | str = .0) -> None:
        if isinstance(time, int):
            time = float(time)
        if isinstance(time, float):
            self._seconds = time
            self._timestamp = Timestamp.seconds_to_timestamp(time)
        elif isinstance(time, str):
            self._timestamp = time
            self._seconds = Timestamp.timestamp_to_seconds(time)
        else:
            raise TypeError()


class VideoInfo():
    stream_url: str = None
    duration: float = None
    title: str  = None
    video_format: str = None
    quality: str = None
    width: int = None
    height: int = None
    fps: int = None
    container: str = None
    protocol: str = None
    aspect_ratio: str = None
    resolution: str = None
    
    def __str__(self) -> str:
        return f'VideoInfo[{self.title}]: {self.duration}s {Timestamp(self.duration)} ' \
               f'({self.video_format}) w:{self.width},h:{self.height}, q:{self.quality}, '\
               f'{self.fps} fps, [{self.container}:{self.protocol}], ratio: ' \
               f'{self.aspect_ratio}, {self.resolution})'


def _get_best_video(yt_dlp_entry: dict, quality: int = 720) -> VideoInfo:
    video_info = VideoInfo()
    best: VideoInfo = None
    min_height: int = None
    best_fps: int = 0

    duration = yt_dlp_entry.get('duration', None)  # Duração em segundos

    #print(yt_dlp_entry.keys())
    duration = yt_dlp_entry.get('duration', None)  # Duração em segundos
    video_info.title = yt_dlp_entry.get('fulltitle', None)

    if duration is None:
        raise RuntimeError('Video duration not found.')
    video_info.duration = float(duration)
    if video_info.title is None:
        raise RuntimeError('Video title not found.')

    video_info.title = yt_dlp_entry.get('fulltitle', None)
    
    for format_dict in yt_dlp_entry['formats']:
        #print(format_dict.keys(), end='\n\n')

        height = format_dict.get('height', None)
        width = format_dict.get('width', None)
        if height is not None and width is not None and height >= quality:
            video_info.stream_url = format_dict.get('url', None)
            video_info.video_format = format_dict.get('format', None)
            video_info.quality = format_dict.get('quality', None)
            video_info.width = format_dict.get('width', None)
            video_info.height = format_dict.get('height', None)
            video_info.fps = format_dict.get('fps', None)
            video_info.container = format_dict.get('container', None)
            video_info.protocol = format_dict.get('protocol', None)
            video_info.resolution = format_dict.get('resolution', None)
            video_info.aspect_ratio = format_dict.get('aspect_ratio', None)

            if video_info.container is None or video_info.container != 'webm_dash' and video_info.container != 'mp4_dash':
                #print(video_info.container)
                continue

            if min_height is None:
                min_height = video_info.height

            #print(video_info, end='\n\n')
            if height == min_height:
                if video_info.fps > best_fps:
                    best = video_info
                    best_fps = video_info.fps
            #elif height > min_height:
                #continue
            #else:
                #print(format_dict.get('url', None))

    if best is None:
        raise RuntimeError(f'Video webm_dash at {quality}p not found')
    elif best.stream_url is None:
        raise RuntimeError('Stream url not found.')
    else:
        if best.video_format is None:
            warn('Video Format not found.')
        if best.quality is None:
            warn('Quality not found.')
        if best.fps is None:
            warn('FPS not found.')
        if best.video_format is None:
            warn('Video Format not found.')
        if best.protocol is None:
            warn('Protocol not found.')
        if best.resolution is None:
            warn('Resolution not found.')
        if best.container is None:
            warn('Video Container not found.')

    return best


def get_video_info(youtube_url, quality: int = 720) -> VideoInfo:
    '''
    Obtém a URL do stream de vídeo e outras informações usando yt-dlp.
    '''
    best: VideoInfo
    ydl_opts = {
        # Escolhe o formato de imagem definido com o melhor áudio disponível
        'format': f'bestvideo[height>={quality}p]+bestaudio/best',
        'quiet': True,     # Silencia a saída do yt-dlp
        'noplaylist': True # Não baixa playlists
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False)
        
        _type = info_dict.get('_type', None)
        
        if _type is None:
            err('Atribute _type not found')
        elif type != 'video':
            err(f'{youtube_url} is not a valid yt video url!')
            exit(4)

        best = _get_best_video(yt_dlp, quality)

    warn(best)

    return best


class PlaylistInfo:
    videos: list[VideoInfo]
    total_duration: int = 0
    
    def __init__(self) -> None:
        self.videos = list()


def get_playlist_info(youtube_url, quality: int = 720) -> PlaylistInfo:
    '''
    Obtém informações dos vídeos em uma playlist do YouTube usando yt-dlp.
    '''
    playlist_info = PlaylistInfo()

    ydl_opts = {
        'format': f'bestvideo[height>={quality}p]+bestaudio/best',
        'quiet': False,
        'extract_flat': False,  # Para extrair informações completas dos vídeos
        'noplaylist': False     # Ativa o modo de playlist
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_dict = ydl.extract_info(youtube_url, download=False)
        _type = playlist_dict.get('_type', None)

        if _type is None:
            err('Atribute _type not found')
        elif _type != 'playlist':
            err(f'{youtube_url} is not a valid yt playlist url!')
            exit(4)

        if 'entries' not in playlist_dict:
            raise RuntimeError('Playlist entries not found.')

        for entry in playlist_dict['entries']:
            best: VideoInfo = _get_best_video(entry)
            
            # Soma a duração de cada vídeo à duração total da playlist
            playlist_info.total_duration += best.duration
            
            # Adiciona o vídeo à lista de vídeos da playlist
            playlist_info.videos.append(best)

    return playlist_info


def _generate_output_folder(path: str) -> None:
    if os.path.exists(path):
        if not os.path.isdir(path):
            err(f'{path} argument is not a valid directory.')
            exit(2)
    else:
        os.makedirs(path)
        log(f'Directory {path} created!')


# Função que extrai um único frame do vídeo no timestamp especificado diretamente da stream.
def capture_frame_at_timestamp(stream_url, timestamp: Timestamp, name: str = "frame",
                               output_format: str = 'png', output_folder: str | None = None):
    output_file: str = f'{name} {timestamp.as_file_name()}.{output_format}'
    output_path: str = os.path.join(output_folder, output_file) if \
        output_folder is not None else output_file

    #command: list = [
    #    'ffmpeg', '-ss', timestamp.timestamp, '-i', stream_url, '-frames:v', '1', '-q:v', '2', output_file
    #]
    command = [
        'ffmpeg', '-ss', timestamp.timestamp, '-i', stream_url,
        '-reconnect', '1',             # Habilitar reconexão
        '-reconnect_streamed', '1',    # Reconexão para stream ao vivo
        '-reconnect_delay_max', '5',   # Máximo de delay entre tentativas de reconexão
        '-frames:v', '1', '-q:v', '2', output_path
    ]

    with open(f'{output_path}.log', 'w') as log_file:
        complete=subprocess.run(command, stderr=log_file)
        if complete.returncode != 0:
            input(f'Error {complete.returncode}...')
        else:
            log(f"Captured frame at {timestamp} and saved as {output_file}")


def calculate_timestamps(duration: float, n_screenshots: int, offset: float = 0.,
                         portion_offset: float = 0.) -> list[Timestamp]:
    '''
    Função para gerar os timestamps com base na duração e no número de screenshots.
    @params:
        offset: how many seconds to ignore from video start.
    '''
    interval = (duration - offset) / n_screenshots  # Intervalo em segundos
    offset += interval * portion_offset
    timestamps = [Timestamp(i * interval + offset) for i in range(n_screenshots)]
    return timestamps


class PlaylistTimestamps():
    _times: list[tuple[VideoInfo, list[Timestamp]]]
    _video: int = 0
    _stamp: int = 0
    
    def __iter__(self):
        return self
    
    def __next__(self) -> tuple[VideoInfo, Timestamp]:
        video, stamps = self._times[self._video]
        
        if self._stamp < len(stamps):
            item = stamps[self._stamp]
            self._stamp += 1
            return video, item
        elif self._video + 1 < len(self._times):
            self._stamp = 1
            self._video += 1
            video, stamps = self._times[self._video]
            return video, stamps[0]
        else:
            raise StopIteration

    def __init__(self, playlist: PlaylistInfo, stamps_n: int,
                                portion_offset: float = 0.) -> None:
        self._times = list()
        frequency: float = playlist.total_duration / stamps_n
        cursor: float = frequency * portion_offset
        count: float = 0.

        for video in playlist.videos:
            print(video)
            timestamp = Timestamp(cursor - count)
            if timestamp <= video.duration:
                timestamps = [timestamp]

                while timestamp <= video.duration:
                    timestamps.append(timestamp)
                    cursor += frequency
                    timestamp = Timestamp(cursor - count)

                self._times.append((video, timestamps))
            count += video.duration


DEFAULT_SCREENSHOTS_N: int = 100
def main(youtube_url: str = "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
         timestamp: list[Timestamp] | None = None,
         screenshots_n: int = DEFAULT_SCREENSHOTS_N,
         output_folder: str = 'frames',
         portion_offset: float = 0.,
         offset: float = 0.) -> None:
    '''
    @params:
        url: URL do vídeo do YouTube e número de screenshots desejadas
        output_folder: caminho do diretório onde os arquivos serão salvos.
        -t timestamp: lista de tempos no formato dd hh:mm:ss separados por
        vírgula.
        -n screenshots_n: quantidade de capturas a serem retiradas de forma
        distribuída ao longo do vídeo.
        -p portion_offset: porção de deslocamento (%) em relação à frequência
        homogênea.
        +<float> offset: quantos segundos serão ignorados no início do vídeo.
    '''
    # Passo 0: Verificar o tipo de download:
    is_playlist: bool
    match identify_youtube_url_type(youtube_url):
        case YT_URL_TYPE.VIDEO:
            is_playlist = False
        case YT_URL_TYPE.PLAYLIST:
            is_playlist = True
        case YT_URL_TYPE.VIDEO_IN_PLAYLIST:
            warn('The url passed is a video in a playlist.')
            is_playlist = input('Do you want to scan all the playlist? [Y, n] ').strip()[:1].lower() != 'n'
        case YT_URL_TYPE.UNKNOWN:
            err('The url is unknown.')
            exit(5)
    
    _generate_output_folder(output_folder)
    warn(f'Saving screenshots at "{output_folder}"')
    
    if is_playlist:
        # Passo 1: Obter informações sobre a playlist
        info: PlaylistInfo = get_playlist_info(youtube_url)
        log(f"Duração da playlist: {info.total_duration} segundos")
        
        if timestamp:
            # TODO -> Make it work?
            warn('option -t does not work with playlists. timestamps ignored')

        playlist_timestamps = PlaylistTimestamps(info, screenshots_n, offset)

        for video, time in playlist_timestamps:
            capture_frame_at_timestamp(
                video.stream_url, time, output_folder=output_folder)
            print(video, time)
    else:
        # Passo 1: Obter stream e duração do vídeo
        info: VideoInfo = get_video_info(youtube_url)
        log(f"Duração do vídeo: {info.duration} segundos")

        if not timestamp:
            # Passo 2: Calcular os timestamps igualmente espaçados.
            timestamp = calculate_timestamps(
                info.duration, screenshots_n, offset, portion_offset)
            log(f"Timestamps calculados:")
            STAMP_LEN: str = len(str(Timestamp()))
            cols: int = os.environ.GET('COLUMNS', 60) / (STAMP_LEN + 1)
            rows: int = len(timestamp) / cols
            for i in range(rows):
                print(*timestamp[i * rows:i * rows + cols])
            offset = 0.

        if timestamp:
            # Passo 3: Capturar frames diretamente do stream nos tempos dados.
            for time in timestamp:
                time += offset
                warn(time)
                #print(info.stream_url)
                capture_frame_at_timestamp(
                    info.stream_url, time, output_folder=output_folder)



if __name__ == "__main__":
    args_n: int = len(sys.argv)
    if args_n > 1:
        options: dict = {}
        i: int = 1
        while i < args_n:
            match sys.argv[i]:
                case '-t':
                    if args_n > i + 1:
                        options['timestamp'] = [ Timestamp(timestamp) for timestamp in sys.argv[i + 1].split(',') ]
                        i += 1
                    else:
                        err('No timestamp set. Use dd hh:mm:ss format.')
                        exit(1)
                case '-n':
                    if args_n > i + 1:
                        options['screenshots_n'] = int(sys.argv[i + 1])
                        i += 1
                    else:
                        warn(F'N° of screenshots not defined. Fallback to default ({DEFAULT_SCREENSHOTS_N}).')
                case '-p':
                    if args_n > i + 1:
                        p = float(sys.argv[i + 1])
                        if 0.0 > p > 1.0:
                            warn('portion must be a value in the interval [0.0, 1.0]. Truncate!')
                            p %= 1.0
                        options['portion_offset'] = p
                        i += 1
                    else:
                        warn(F'Offset ratio not defined. Fallback to default ({DEFAULT_SCREENSHOTS_N}).')
                case var:
                    if var.startswith('+'):
                        options['offset'] = float(var)
                    elif is_valid_youtube_url(var):
                        options['youtube_url'] = var
                    elif is_valid_url(var):
                        warn('The given url is not a youtube url, may not work.')
                        options['youtube_url'] = var
                    else:
                        options['output_folder'] = var
            i += 1

        if 'youtube_url' not in options.keys():
            warn('url not set, fallback to default')

        main(**options)
    else:
        print(main.__doc__)
