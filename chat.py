
class Chat:

    START_TEXT = """ ආයුබෝවන් (❤ {first} ❤) !!!! 🙏🙏🙏

* ගොඩක් අය හොයන දෙයක් තමයි telegram එකෙන් ගත්ත film එකකට උපසිරැසි file එක set කරගන්නේ කොහොමද කියන එක. 

* මේ ප්‍රශ්නේ තියෙන්නේ phone වලින් film බලන අයට තමයි.

* මේ bot ට පුලුවන් අපේ <b>video file</b> එකට <b>subtitle file</b>(.ass file or .srt file) එක ලස්සනට set කරලා දෙන්න.😎

<b>📽🎬📽Send me a Telegram file to begin Or forward your video file for me📽🎬📽</b>

/help for more details..

Credits :- @senithlokitha_chat_bot
    """

    HELP_USER = "??"

    HELP_TEXT ="""<b>Welcome to the Help Menu</b>

* ගොඩක් අය හොයන දෙයක් තමයි telegram එකෙන් ගත්ත film එකකට උපසිරැසි file එක set කරගන්නේ කොහොමද කියන එක. 
* මේ ප්‍රශ්නේ තියෙන්නේ phone වලින් film බලන අයට තමයි.
* මේ bot ට පුලුවන් අපේ video file එකට subtitle file(.ass file or .srt file) එක ලස්සනට set කරලා දෙන්න.

*(❤ {first} ❤) අපි බලමු කොහොමද ඔයගේ film එකට sub file එක set කරන්නෙ 

1.) මුලින්ම ඔයගේ film එක හෝ film eke link එක එවන්න.
<b>File downloaded successfully!</b> message එක එනකන් ඉන්න.❗❗❗
2.) දැන් ඔයාගේ sub file එක එවන්න (zip file එවලා පිස්සු නටන්න එපා.srt file හරි ass file එවන්න.❗❗❗)
<b>Subtitle file downloaded successfully!</b> message එක එනකන් ඉන්න.❗❗❗
3.) දැන් තමයි sub file එකයි film එකයි mix කරන්න තියෙන්නෙ \nමෙතනදි ඔයා දීපු sub file එකේ front එක ගැන සැලකිලිමත් වෙන්න ඕන. සිංහල subtitle එකක් නම් /softremove කියන command එක දෙන්න.english subtitle එකක් නම් /hardmux කියන command එක දෙන්න.!
\n <b>NOTE:-</b><i>ෆිල්ම් එකෙ තියෙන අනවශ්‍ය stream files[english sub or eny other] remove කරන්න /softmux command එක භාවිතා කරන්න❗❗❗ </i>
To give custom name to file send it with url seperated with |
<i>url|custom_name.mp4</i>

<b>Note : </b><i>Please note that only english type fonts are supported in hardmux other scripts will be shown as empty blocks on the video!</i>

<a href="https://t.me/senithlokitha_chat_bot">Report error</a>"""

    NO_AUTH_USER = "(❤ {first} ❤) මේ bot ව භාවිතා කරන්න බෑ.❌❌❌\nමොකද මෙ bot හදලා තියෙන්නේ bot use\n කරන්න ඕන කියලා කියපු අයට"
    DOWNLOAD_SUCCESS = """File downloaded successfully!

Time taken : {} seconds."""
    FILE_SIZE_ERROR = "ERROR ❌❌❌ : Cannot Extract File Size from URL![මේ link එක බොට්ට හොයා ගන්න බැලූ sorry ]"
    MAX_FILE_SIZE = "File size is greater than 2Gb. Which is the limit imposed by telegram!"
    LONG_CUS_FILENAME = """Filename you provided is greater than 60 characters.
Please provide a shorter name."""
    UNSUPPORTED_FORMAT = "ERROR ❌❌❌ : File format {} Not supported!"
    CHOOSE_CMD = "Subtitle file downloaded successfully!.\nChoose your desired mixing!\n[ /softremove , /softmux , /hardmux ]\n<b>NOTE:-</b>\n සිංහල subtitle එකක් නම් /softremove කියන command එක දෙන්න.english subtitle එකක් නම් /hardmux කියන command එක දෙන්න.!!!"