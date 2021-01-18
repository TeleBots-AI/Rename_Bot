from sample_config import Config

class Translation(object):
    START_TEXT = """Hello <i><b>{}</b></i>,

This is a Telegram Rename Bot Devloped <a href='https://t.me/TeleBotinC'>TeleBots</a> by {}

I can rename ✍ your files with custom thumbnail and upload as video/file as directed.

Type /help now for more details."""
    RENAME_403_ERR = "Sorry dear! You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "There is no upgrade plan till now it will be added in future"
    DOWNLOAD_START_VIDEO = "Downloading to my server.....📥"
    DOWNLOAD_START = "Downloading to my server.....📥"
    UPLOAD_START_VIDEO = "Uploading as video.....📤"
    UPLOAD_START = "Uploading as File.....📤"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations.I can't do anything for that 🤷‍♂️."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using [TeleBots](https://t.me/TeleBotinC)'s bot.**"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://t.me/TeleBots_Chats'>TeleBots Support</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom File thumbnail saved ✅️ . This image will be deleted with in 24hr"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = "@TeleRenames_Bot"
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    HELP_USER = """Hai <b><i>{}</i></b>, 
 EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/TheUseLessGroup'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    GET_LINK_ERRS_OCCURED = "Sorry the following Errors occurred: \n{}\nPlease check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/TheUseLessGroup'>@SpEcHlDe</a>"
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
I am Renamer bot ✍ by <a href='https://t.me/{}'>My Father 👨‍🏫</a>
    
1. Send Me A Thumbnail.

2. Send me the file to be Renamed.

3. Reply to that message with <code>/rename new name.extension</code>. with custom thumbnail support.\n(upload as file)

4. Reply to that message with <code>/rename_vidoe new name.extension</code>. with custom thumbnail support.\n(uploading as Video)

   
<b>Thanks to <i><a href="https://t.me/TeleBotsDev">ᴛᴇʟᴇ!ʙᴏᴛs</a></i> for devloped bot. check /about for rename bot</b>

--------

Support Group : @TeleBots_Chats"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to `/rename New Name.extension` with custom thumbnail support.\n\n(For uploading as file).\n\nSee /help for mor information. "
    REPLY_TO_DOC_FOR_RENAME_VIDEO = "Reply to a Telegram media to `/rename_video New Name.extension` with custom thumbnail support.\n\n(For uploading as video).\n\nSee /help for mor information."
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.

<b>Essays Not allowed in Telegram file name!</b>
©️ <code>@TeleRenames_Bot</code>
Please short your file name and try again!"""

    About = """Hi __{}__,

**📝 Language:** Python 3

**🧰 Framework:** Pyrogram

**👨‍💻 Developer:** [</>ᴛᴇʟᴇ/!ʙᴏᴛs</>](https://t.me/TeleBotsDev)

**📮 Channel:** [Telebots Updates](https://t.me/TeleBotInC)

**👥 Group:** [TeleBots Chat](https://t.me/TeleBots_Chats)"""
