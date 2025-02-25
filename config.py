from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("13303918"))
API_HASH = getenv("24f473f4478796b9a416e4e68b49ab25")

BOT_TOKEN = getenv("BOT_TOKEN", "6839471362:AAEejQnQ3wxuRsMy18FKfq-pplEzO5G9d4U")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("13303918"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BQDLAG4AXMbnSpqwA3JXNhnQR99UcpLQUWd8TZH68BNJw6VZOefq78Bpn3EK5apDin65PM62X5Sb5bArhJF_n0DfPNmTEi4duvLLn4AZ-65XzkBGkbbth8FYLmm7vofr1pFZErPWJPVWzTgtPEnJ8TSVYNE_XnR38VXUjxsvWDIPcw1q4KUsMWHVo16I0wwNnt-2NxujDB-idUPYlrIKNeIPCTdC24T80jJkcIC7eA9LRQemHRUBT-KwUD28MIgAd8Qo6Wr9sCzq5loiYJdGRtSgWfcd6m6pxYK9VG7I_f8oCfUZti2q86gqkz31OG3YWm1AGfu_2PP-mSheE4qJudpA7-M6egAAAAA2mX5BAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5094761774 8092453704").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
