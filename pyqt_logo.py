import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QScrollArea
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt
import enum


class QIconWrapper:
    class ThemeIcon(enum.Enum):
        AddressBookNew = ...  # type: QIcon.ThemeIcon
        ApplicationExit = ...  # type: QIcon.ThemeIcon
        AppointmentNew = ...  # type: QIcon.ThemeIcon
        CallStart = ...  # type: QIcon.ThemeIcon
        CallStop = ...  # type: QIcon.ThemeIcon
        ContactNew = ...  # type: QIcon.ThemeIcon
        DocumentNew = ...  # type: QIcon.ThemeIcon
        DocumentOpen = ...  # type: QIcon.ThemeIcon
        DocumentOpenRecent = ...  # type: QIcon.ThemeIcon
        DocumentPageSetup = ...  # type: QIcon.ThemeIcon
        DocumentPrint = ...  # type: QIcon.ThemeIcon
        DocumentPrintPreview = ...  # type: QIcon.ThemeIcon
        DocumentProperties = ...  # type: QIcon.ThemeIcon
        DocumentRevert = ...  # type: QIcon.ThemeIcon
        DocumentSave = ...  # type: QIcon.ThemeIcon
        DocumentSaveAs = ...  # type: QIcon.ThemeIcon
        DocumentSend = ...  # type: QIcon.ThemeIcon
        EditClear = ...  # type: QIcon.ThemeIcon
        EditCopy = ...  # type: QIcon.ThemeIcon
        EditCut = ...  # type: QIcon.ThemeIcon
        EditDelete = ...  # type: QIcon.ThemeIcon
        EditFind = ...  # type: QIcon.ThemeIcon
        EditPaste = ...  # type: QIcon.ThemeIcon
        EditRedo = ...  # type: QIcon.ThemeIcon
        EditSelectAll = ...  # type: QIcon.ThemeIcon
        EditUndo = ...  # type: QIcon.ThemeIcon
        FolderNew = ...  # type: QIcon.ThemeIcon
        FormatIndentLess = ...  # type: QIcon.ThemeIcon
        FormatIndentMore = ...  # type: QIcon.ThemeIcon
        FormatJustifyCenter = ...  # type: QIcon.ThemeIcon
        FormatJustifyFill = ...  # type: QIcon.ThemeIcon
        FormatJustifyLeft = ...  # type: QIcon.ThemeIcon
        FormatJustifyRight = ...  # type: QIcon.ThemeIcon
        FormatTextDirectionLtr = ...  # type: QIcon.ThemeIcon
        FormatTextDirectionRtl = ...  # type: QIcon.ThemeIcon
        FormatTextBold = ...  # type: QIcon.ThemeIcon
        FormatTextItalic = ...  # type: QIcon.ThemeIcon
        FormatTextUnderline = ...  # type: QIcon.ThemeIcon
        FormatTextStrikethrough = ...  # type: QIcon.ThemeIcon
        GoDown = ...  # type: QIcon.ThemeIcon
        GoHome = ...  # type: QIcon.ThemeIcon
        GoNext = ...  # type: QIcon.ThemeIcon
        GoPrevious = ...  # type: QIcon.ThemeIcon
        GoUp = ...  # type: QIcon.ThemeIcon
        HelpAbout = ...  # type: QIcon.ThemeIcon
        HelpFaq = ...  # type: QIcon.ThemeIcon
        InsertImage = ...  # type: QIcon.ThemeIcon
        InsertLink = ...  # type: QIcon.ThemeIcon
        InsertText = ...  # type: QIcon.ThemeIcon
        ListAdd = ...  # type: QIcon.ThemeIcon
        ListRemove = ...  # type: QIcon.ThemeIcon
        MailForward = ...  # type: QIcon.ThemeIcon
        MailMarkImportant = ...  # type: QIcon.ThemeIcon
        MailMarkRead = ...  # type: QIcon.ThemeIcon
        MailMarkUnread = ...  # type: QIcon.ThemeIcon
        MailMessageNew = ...  # type: QIcon.ThemeIcon
        MailReplyAll = ...  # type: QIcon.ThemeIcon
        MailReplySender = ...  # type: QIcon.ThemeIcon
        MailSend = ...  # type: QIcon.ThemeIcon
        MediaEject = ...  # type: QIcon.ThemeIcon
        MediaPlaybackPause = ...  # type: QIcon.ThemeIcon
        MediaPlaybackStart = ...  # type: QIcon.ThemeIcon
        MediaPlaybackStop = ...  # type: QIcon.ThemeIcon
        MediaRecord = ...  # type: QIcon.ThemeIcon
        MediaSeekBackward = ...  # type: QIcon.ThemeIcon
        MediaSeekForward = ...  # type: QIcon.ThemeIcon
        MediaSkipBackward = ...  # type: QIcon.ThemeIcon
        MediaSkipForward = ...  # type: QIcon.ThemeIcon
        ObjectRotateLeft = ...  # type: QIcon.ThemeIcon
        ObjectRotateRight = ...  # type: QIcon.ThemeIcon
        ProcessStop = ...  # type: QIcon.ThemeIcon
        SystemLockScreen = ...  # type: QIcon.ThemeIcon
        SystemLogOut = ...  # type: QIcon.ThemeIcon
        SystemSearch = ...  # type: QIcon.ThemeIcon
        SystemReboot = ...  # type: QIcon.ThemeIcon
        SystemShutdown = ...  # type: QIcon.ThemeIcon
        ToolsCheckSpelling = ...  # type: QIcon.ThemeIcon
        ViewFullscreen = ...  # type: QIcon.ThemeIcon
        ViewRefresh = ...  # type: QIcon.ThemeIcon
        ViewRestore = ...  # type: QIcon.ThemeIcon
        WindowClose = ...  # type: QIcon.ThemeIcon
        WindowNew = ...  # type: QIcon.ThemeIcon
        ZoomFitBest = ...  # type: QIcon.ThemeIcon
        ZoomIn = ...  # type: QIcon.ThemeIcon
        ZoomOut = ...  # type: QIcon.ThemeIcon
        AudioCard = ...  # type: QIcon.ThemeIcon
        AudioInputMicrophone = ...  # type: QIcon.ThemeIcon
        Battery = ...  # type: QIcon.ThemeIcon
        CameraPhoto = ...  # type: QIcon.ThemeIcon
        CameraVideo = ...  # type: QIcon.ThemeIcon
        CameraWeb = ...  # type: QIcon.ThemeIcon
        Computer = ...  # type: QIcon.ThemeIcon
        DriveHarddisk = ...  # type: QIcon.ThemeIcon
        DriveOptical = ...  # type: QIcon.ThemeIcon
        InputGaming = ...  # type: QIcon.ThemeIcon
        InputKeyboard = ...  # type: QIcon.ThemeIcon
        InputMouse = ...  # type: QIcon.ThemeIcon
        InputTablet = ...  # type: QIcon.ThemeIcon
        MediaFlash = ...  # type: QIcon.ThemeIcon
        MediaOptical = ...  # type: QIcon.ThemeIcon
        MediaTape = ...  # type: QIcon.ThemeIcon
        MultimediaPlayer = ...  # type: QIcon.ThemeIcon
        NetworkWired = ...  # type: QIcon.ThemeIcon
        NetworkWireless = ...  # type: QIcon.ThemeIcon
        Phone = ...  # type: QIcon.ThemeIcon
        Printer = ...  # type: QIcon.ThemeIcon
        Scanner = ...  # type: QIcon.ThemeIcon
        VideoDisplay = ...  # type: QIcon.ThemeIcon
        AppointmentMissed = ...  # type: QIcon.ThemeIcon
        AppointmentSoon = ...  # type: QIcon.ThemeIcon
        AudioVolumeHigh = ...  # type: QIcon.ThemeIcon
        AudioVolumeLow = ...  # type: QIcon.ThemeIcon
        AudioVolumeMedium = ...  # type: QIcon.ThemeIcon
        AudioVolumeMuted = ...  # type: QIcon.ThemeIcon
        BatteryCaution = ...  # type: QIcon.ThemeIcon
        BatteryLow = ...  # type: QIcon.ThemeIcon
        DialogError = ...  # type: QIcon.ThemeIcon
        DialogInformation = ...  # type: QIcon.ThemeIcon
        DialogPassword = ...  # type: QIcon.ThemeIcon
        DialogQuestion = ...  # type: QIcon.ThemeIcon
        DialogWarning = ...  # type: QIcon.ThemeIcon
        FolderDragAccept = ...  # type: QIcon.ThemeIcon
        FolderOpen = ...  # type: QIcon.ThemeIcon
        FolderVisiting = ...  # type: QIcon.ThemeIcon
        ImageLoading = ...  # type: QIcon.ThemeIcon
        ImageMissing = ...  # type: QIcon.ThemeIcon
        MailAttachment = ...  # type: QIcon.ThemeIcon
        MailUnread = ...  # type: QIcon.ThemeIcon
        MailRead = ...  # type: QIcon.ThemeIcon
        MailReplied = ...  # type: QIcon.ThemeIcon
        MediaPlaylistRepeat = ...  # type: QIcon.ThemeIcon
        MediaPlaylistShuffle = ...  # type: QIcon.ThemeIcon
        NetworkOffline = ...  # type: QIcon.ThemeIcon
        PrinterPrinting = ...  # type: QIcon.ThemeIcon
        SecurityHigh = ...  # type: QIcon.ThemeIcon
        SecurityLow = ...  # type: QIcon.ThemeIcon
        SoftwareUpdateAvailable = ...  # type: QIcon.ThemeIcon
        SoftwareUpdateUrgent = ...  # type: QIcon.ThemeIcon
        SyncError = ...  # type: QIcon.ThemeIcon
        SyncSynchronizing = ...  # type: QIcon.ThemeIcon
        UserAvailable = ...  # type: QIcon.ThemeIcon
        UserOffline = ...  # type: QIcon.ThemeIcon
        WeatherClear = ...  # type: QIcon.ThemeIcon
        WeatherClearNight = ...  # type: QIcon.ThemeIcon
        WeatherFewClouds = ...  # type: QIcon.ThemeIcon
        WeatherFewCloudsNight = ...  # type: QIcon.ThemeIcon
        WeatherFog = ...  # type: QIcon.ThemeIcon
        WeatherShowers = ...  # type: QIcon.ThemeIcon
        WeatherSnow = ...  # type: QIcon.ThemeIcon
        WeatherStorm = ...  # type: QIcon.ThemeIcon


class IconDisplayApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # 创建一个容器widget来包含网格布局
        container = QWidget()
        grid_layout = QGridLayout()
        row = 0
        col = 0

        # 获取所有可用的主题图标名称
        theme_icons = [
    'address-book-new', 'application-exit', 'appointment-new', 'call-start', 'call-stop', 'contact-new', 'document-new',
    'document-open', 'document-open-recent', 'document-page-setup', 'document-print', 'document-print-preview',
    'document-properties', 'document-revert', 'document-save', 'document-save-as', 'document-send', 'edit-clear',
    'edit-copy', 'edit-cut', 'edit-delete', 'edit-find', 'edit-paste', 'edit-redo', 'edit-select-all', 'edit-undo',
    'folder-new', 'format-indent-less', 'format-indent-more', 'format-justify-center', 'format-justify-fill',
    'format-justify-left', 'format-justify-right', 'format-text-direction-ltr', 'format-text-direction-rtl',
    'format-text-bold', 'format-text-italic', 'format-text-underline', 'format-text-strikethrough', 'go-down',
    'go-home', 'go-next', 'go-previous', 'go-up', 'help-about', 'help-faq', 'insert-image', 'insert-link',
    'insert-text', 'list-add', 'list-remove', 'mail-forward', 'mail-mark-important', 'mail-mark-read',
    'mail-mark-unread', 'mail-message-new', 'mail-reply-all', 'mail-reply-sender', 'mail-send', 'media-eject',
    'media-playback-pause', 'media-playback-start', 'media-playback-stop', 'media-record', 'media-seek-backward',
    'media-seek-forward', 'media-skip-backward', 'media-skip-forward', 'object-rotate-left', 'object-rotate-right',
    'process-stop', 'system-lock-screen', 'system-log-out', 'system-search', 'system-reboot', 'system-shutdown',
    'tools-check-spelling', 'view-fullscreen', 'view-refresh', 'view-restore', 'window-close', 'window-new',
    'zoom-fit-best', 'zoom-in', 'zoom-out', 'audio-card', 'audio-input-microphone', 'battery', 'camera-photo',
    'camera-video', 'camera-web', 'computer', 'drive-harddisk', 'drive-optical', 'input-gaming', 'input-keyboard',
    'input-mouse', 'input-tablet', 'media-flash', 'media-optical', 'media-tape', 'multimedia-player',
    'network-wired', 'network-wireless', 'phone', 'printer', 'scanner', 'video-display', 'appointment-missed',
    'appointment-soon', 'audio-volume-high', 'audio-volume-low', 'audio-volume-medium', 'audio-volume-muted',
    'battery-caution', 'battery-low', 'dialog-error', 'dialog-information', 'dialog-password', 'dialog-question',
    'dialog-warning', 'folder-drag-accept', 'folder-open', 'folder-visiting', 'image-loading', 'image-missing',
    'mail-attachment', 'mail-unread', 'mail-read', 'mail-replied', 'media-playlist-repeat', 'media-playlist-shuffle',
    'network-offline', 'printer-printing', 'security-high', 'security-low', 'software-update-available',
    'software-update-urgent', 'sync-error', 'sync-synchronizing', 'user-available', 'user-offline', 'weather-clear',
    'weather-clear-night', 'weather-few-clouds', 'weather-few-clouds-night', 'weather-fog', 'weather-showers',
    'weather-snow', 'weather-storm'
]

        for icon_name in theme_icons:
            icon = QIcon.fromTheme(icon_name)
            if not icon.isNull():
                label_icon = QLabel()
                label_icon.setPixmap(icon.pixmap(QSize(32, 32)))
                label_name = QLabel(icon_name)
                label_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

                grid_layout.addWidget(label_icon, row, col)
                grid_layout.addWidget(label_name, row + 1, col)

                col += 1
                if col >= 5:  # 每行显示5个图标
                    col = 0
                    row += 2

        container.setLayout(grid_layout)

        # 创建滚动区域
        scroll = QScrollArea()
        scroll.setWidget(container)
        scroll.setWidgetResizable(True)
        
        # 为主窗口设置滚动区域
        main_layout = QGridLayout()
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)
        
        self.setWindowTitle("PyQt6 自带图标展示")
        self.resize(800, 600)  # 调整窗口大小以适应更多图标


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IconDisplayApp()
    window.show()
    sys.exit(app.exec())