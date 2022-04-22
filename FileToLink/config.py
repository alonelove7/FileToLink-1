import os


class Config:
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    Token = os.environ.get("BOT_TOKEN")
    Session = os.environ.get("Session_String")
    if Session is None or Session == "":
        Session = ":memory:"
    App_Name = os.environ.get("APP_NAME")
    Port = int(os.environ.get("PORT"))
    Archive_Channel_ID = int(os.environ.get("ARCHIVE_CHANNEL_ID"))
    Start_Message = os.environ.get("Start_Message")
    Bot_Channel = os.environ.get("Bot_Channel_UserName")
    if Bot_Channel and Bot_Channel.startswith("@"):
        Bot_Channel = Bot_Channel[1:]
    elif Bot_Channel == "":
        Bot_Channel = None

    Link_Root = f"https://{App_Name}.herokuapp.com/"
    Download_Folder = "Files"
    Dev_Channel = "UploadFreeChanel"
    Bot_UserName = None  # The bot will set it after starting
    Part_size = 10 * 1024 * 1024  # (10MB) For Pyrogram
    Buffer_Size = 512 * 1024  # For Quart
    Pre_Dl = 3  # How many parts to download from telegram before client request them
    Separate_Time = 4  # (seconds)  wait time between messages if user send more than one
    Sleep_Threshold = 60  # (Seconds) sleep threshold for flood wait exceptions
    Max_Fast_Processes = 1  # How many links user can update them to fast links at the same time


class Strings:
    start = Config.Start_Message
    dl_link = "🔗Descargar enlace"
    st_link = "🎞 Enlace directo..."
    generating_link = "**⏳ Creando enlace...**"
    bot_channel = "📢 Canal del Bot"
    dev_channel = "🤖Canal Oficial"
    fast = "⚡️**El enlace se ha actualizado a un enlace rápido.**"
    update_link = "⚡Actualizar a enlace rápido"
    update_limited = (f"⛔ Puedes actualizar solo {Config.Max_Fast_Processes} enlace en una sola vez, "
                      "please wait until previous update to complete")
    re_update_link = "🔄 Reevaluando el enlace"
    already_updated = "El enlace ya está actualizado."
    wait_update = "⏳ Actualizando el enlace..."
    wait = "⏳ Espere por favor..."
    progress = "⏳ Progreso"
    file_not_found = "⚠️Archivo no encontrado, por favor reenvíalo de nuevo"
    delete_manually_button = "⚠️Puedes bórrarlo"
    delete_forbidden = "El BOT no puede eliminar mensajes mayores de 48 horas, puede eliminar este mensaje manualmente"
    force_join = "⚠ Únete a Upload Free Chanel para usar este Bot"
