# ひらがな46文字すべての学習データ定義
# 各文字に3つの単語（emoji付き）を設定

# データ構造:
# {
#   "char": ひらがな1文字,
#   "words": [
#     {"word": 単語, "emoji": 絵文字, "keyword_en": 英語キーワード(Pixabay検索用)},
#     ...
#   ]
# }

HIRAGANA_DATA: list[dict] = [
    # あ行
    {
        "char": "あ",
        "words": [
            {"word": "あり", "emoji": "🐜", "keyword_en": "ant"},
            {"word": "あめ", "emoji": "🍬", "keyword_en": "candy"},
            {"word": "あお", "emoji": "🔵", "keyword_en": "blue"},
        ],
    },
    {
        "char": "い",
        "words": [
            {"word": "いぬ", "emoji": "🐶", "keyword_en": "dog"},
            {"word": "いちご", "emoji": "🍓", "keyword_en": "strawberry"},
            {"word": "いす", "emoji": "🪑", "keyword_en": "chair"},
        ],
    },
    {
        "char": "う",
        "words": [
            {"word": "うさぎ", "emoji": "🐰", "keyword_en": "rabbit"},
            {"word": "うみ", "emoji": "🌊", "keyword_en": "sea"},
            {"word": "うし", "emoji": "🐄", "keyword_en": "cow"},
        ],
    },
    {
        "char": "え",
        "words": [
            {"word": "えんぴつ", "emoji": "✏️", "keyword_en": "pencil"},
            {"word": "えび", "emoji": "🦐", "keyword_en": "shrimp"},
            {"word": "えほん", "emoji": "📚", "keyword_en": "picture book"},
        ],
    },
    {
        "char": "お",
        "words": [
            {"word": "おに", "emoji": "👹", "keyword_en": "demon"},
            {"word": "おかし", "emoji": "🍩", "keyword_en": "sweets"},
            {"word": "おはな", "emoji": "🌸", "keyword_en": "flower"},
        ],
    },
    # か行
    {
        "char": "か",
        "words": [
            {"word": "かに", "emoji": "🦀", "keyword_en": "crab"},
            {"word": "かさ", "emoji": "☂️", "keyword_en": "umbrella"},
            {"word": "かめ", "emoji": "🐢", "keyword_en": "turtle"},
        ],
    },
    {
        "char": "き",
        "words": [
            {"word": "きりん", "emoji": "🦒", "keyword_en": "giraffe"},
            {"word": "きつね", "emoji": "🦊", "keyword_en": "fox"},
            {"word": "きのこ", "emoji": "🍄", "keyword_en": "mushroom"},
        ],
    },
    {
        "char": "く",
        "words": [
            {"word": "くま", "emoji": "🐻", "keyword_en": "bear"},
            {"word": "くるま", "emoji": "🚗", "keyword_en": "car"},
            {"word": "くじら", "emoji": "🐋", "keyword_en": "whale"},
        ],
    },
    {
        "char": "け",
        "words": [
            {"word": "けむし", "emoji": "🐛", "keyword_en": "caterpillar"},
            {"word": "けーき", "emoji": "🎂", "keyword_en": "cake"},
            {"word": "けん", "emoji": "⚔️", "keyword_en": "sword"},
        ],
    },
    {
        "char": "こ",
        "words": [
            {"word": "こあら", "emoji": "🐨", "keyword_en": "koala"},
            {"word": "こおり", "emoji": "🧊", "keyword_en": "ice"},
            {"word": "こま", "emoji": "🪀", "keyword_en": "spinning top"},
        ],
    },
    # さ行
    {
        "char": "さ",
        "words": [
            {"word": "さかな", "emoji": "🐟", "keyword_en": "fish"},
            {"word": "さる", "emoji": "🐒", "keyword_en": "monkey"},
            {"word": "さくら", "emoji": "🌸", "keyword_en": "cherry blossom"},
        ],
    },
    {
        "char": "し",
        "words": [
            {"word": "しまうま", "emoji": "🦓", "keyword_en": "zebra"},
            {"word": "しんかんせん", "emoji": "🚅", "keyword_en": "bullet train"},
            {"word": "しろ", "emoji": "🏰", "keyword_en": "castle"},
        ],
    },
    {
        "char": "す",
        "words": [
            {"word": "すいか", "emoji": "🍉", "keyword_en": "watermelon"},
            {"word": "すずめ", "emoji": "🐦", "keyword_en": "sparrow"},
            {"word": "すべりだい", "emoji": "🛝", "keyword_en": "slide"},
        ],
    },
    {
        "char": "せ",
        "words": [
            {"word": "せみ", "emoji": "🦗", "keyword_en": "cicada"},
            {"word": "せんせい", "emoji": "👨‍🏫", "keyword_en": "teacher"},
            {"word": "せっけん", "emoji": "🧼", "keyword_en": "soap"},
        ],
    },
    {
        "char": "そ",
        "words": [
            {"word": "そら", "emoji": "🌤️", "keyword_en": "sky"},
            {"word": "そうじき", "emoji": "🧹", "keyword_en": "broom"},
            {"word": "そろばん", "emoji": "🧮", "keyword_en": "abacus"},
        ],
    },
    # た行
    {
        "char": "た",
        "words": [
            {"word": "たこ", "emoji": "🐙", "keyword_en": "octopus"},
            {"word": "たいこ", "emoji": "🥁", "keyword_en": "drum"},
            {"word": "たまご", "emoji": "🥚", "keyword_en": "egg"},
        ],
    },
    {
        "char": "ち",
        "words": [
            {"word": "ちょうちょ", "emoji": "🦋", "keyword_en": "butterfly"},
            {"word": "ちず", "emoji": "🗺️", "keyword_en": "map"},
            {"word": "ちきゅう", "emoji": "🌍", "keyword_en": "earth"},
        ],
    },
    {
        "char": "つ",
        "words": [
            {"word": "つき", "emoji": "🌙", "keyword_en": "moon"},
            {"word": "つる", "emoji": "🦢", "keyword_en": "crane"},
            {"word": "つみき", "emoji": "🧱", "keyword_en": "blocks"},
        ],
    },
    {
        "char": "て",
        "words": [
            {"word": "てんとうむし", "emoji": "🐞", "keyword_en": "ladybug"},
            {"word": "てつどう", "emoji": "🚂", "keyword_en": "train"},
            {"word": "てぶくろ", "emoji": "🧤", "keyword_en": "gloves"},
        ],
    },
    {
        "char": "と",
        "words": [
            {"word": "とら", "emoji": "🐯", "keyword_en": "tiger"},
            {"word": "とり", "emoji": "🐦", "keyword_en": "bird"},
            {"word": "とまと", "emoji": "🍅", "keyword_en": "tomato"},
        ],
    },
    # な行
    {
        "char": "な",
        "words": [
            {"word": "なす", "emoji": "🍆", "keyword_en": "eggplant"},
            {"word": "なまけもの", "emoji": "🦥", "keyword_en": "sloth"},
            {"word": "なのはな", "emoji": "🌼", "keyword_en": "rapeseed flower"},
        ],
    },
    {
        "char": "に",
        "words": [
            {"word": "にわとり", "emoji": "🐔", "keyword_en": "chicken"},
            {"word": "にじ", "emoji": "🌈", "keyword_en": "rainbow"},
            {"word": "にんじん", "emoji": "🥕", "keyword_en": "carrot"},
        ],
    },
    {
        "char": "ぬ",
        "words": [
            {"word": "ぬいぐるみ", "emoji": "🧸", "keyword_en": "stuffed toy"},
            {"word": "ぬまがえる", "emoji": "🐸", "keyword_en": "frog"},
            {"word": "ぬりえ", "emoji": "🎨", "keyword_en": "coloring"},
        ],
    },
    {
        "char": "ね",
        "words": [
            {"word": "ねこ", "emoji": "🐱", "keyword_en": "cat"},
            {"word": "ねずみ", "emoji": "🐭", "keyword_en": "mouse"},
            {"word": "ねっこ", "emoji": "🌿", "keyword_en": "root"},
        ],
    },
    {
        "char": "の",
        "words": [
            {"word": "のはら", "emoji": "🌾", "keyword_en": "field"},
            {"word": "のりもの", "emoji": "🚌", "keyword_en": "vehicle"},
            {"word": "のこぎり", "emoji": "🪚", "keyword_en": "saw"},
        ],
    },
    # は行
    {
        "char": "は",
        "words": [
            {"word": "はな", "emoji": "🌺", "keyword_en": "flower"},
            {"word": "はち", "emoji": "🐝", "keyword_en": "bee"},
            {"word": "はさみ", "emoji": "✂️", "keyword_en": "scissors"},
        ],
    },
    {
        "char": "ひ",
        "words": [
            {"word": "ひよこ", "emoji": "🐣", "keyword_en": "chick"},
            {"word": "ひこうき", "emoji": "✈️", "keyword_en": "airplane"},
            {"word": "ひまわり", "emoji": "🌻", "keyword_en": "sunflower"},
        ],
    },
    {
        "char": "ふ",
        "words": [
            {"word": "ふね", "emoji": "⛵", "keyword_en": "boat"},
            {"word": "ふうせん", "emoji": "🎈", "keyword_en": "balloon"},
            {"word": "ふくろう", "emoji": "🦉", "keyword_en": "owl"},
        ],
    },
    {
        "char": "へ",
        "words": [
            {"word": "へび", "emoji": "🐍", "keyword_en": "snake"},
            {"word": "ヘルメット", "emoji": "⛑️", "keyword_en": "helmet"},
            {"word": "へいわ", "emoji": "☮️", "keyword_en": "peace"},
        ],
    },
    {
        "char": "ほ",
        "words": [
            {"word": "ほし", "emoji": "⭐", "keyword_en": "star"},
            {"word": "ほん", "emoji": "📖", "keyword_en": "book"},
            {"word": "ほたる", "emoji": "✨", "keyword_en": "firefly"},
        ],
    },
    # ま行
    {
        "char": "ま",
        "words": [
            {"word": "まり", "emoji": "⚽", "keyword_en": "ball"},
            {"word": "まつ", "emoji": "🌲", "keyword_en": "pine tree"},
            {"word": "まんが", "emoji": "📕", "keyword_en": "manga"},
        ],
    },
    {
        "char": "み",
        "words": [
            {"word": "みかん", "emoji": "🍊", "keyword_en": "mandarin orange"},
            {"word": "みず", "emoji": "💧", "keyword_en": "water"},
            {"word": "みつばち", "emoji": "🐝", "keyword_en": "honeybee"},
        ],
    },
    {
        "char": "む",
        "words": [
            {"word": "むし", "emoji": "🐛", "keyword_en": "bug"},
            {"word": "むらさき", "emoji": "💜", "keyword_en": "purple"},
            {"word": "むぎわら", "emoji": "🌾", "keyword_en": "wheat"},
        ],
    },
    {
        "char": "め",
        "words": [
            {"word": "めだか", "emoji": "🐠", "keyword_en": "medaka fish"},
            {"word": "めがね", "emoji": "👓", "keyword_en": "glasses"},
            {"word": "めいろ", "emoji": "🧩", "keyword_en": "maze"},
        ],
    },
    {
        "char": "も",
        "words": [
            {"word": "もも", "emoji": "🍑", "keyword_en": "peach"},
            {"word": "もぐら", "emoji": "🦔", "keyword_en": "mole"},
            {"word": "もり", "emoji": "🌳", "keyword_en": "forest"},
        ],
    },
    # や行
    {
        "char": "や",
        "words": [
            {"word": "やぎ", "emoji": "🐐", "keyword_en": "goat"},
            {"word": "やまいも", "emoji": "🥔", "keyword_en": "yam"},
            {"word": "やね", "emoji": "🏠", "keyword_en": "roof"},
        ],
    },
    {
        "char": "ゆ",
        "words": [
            {"word": "ゆき", "emoji": "❄️", "keyword_en": "snow"},
            {"word": "ゆびわ", "emoji": "💍", "keyword_en": "ring"},
            {"word": "ゆうひ", "emoji": "🌅", "keyword_en": "sunset"},
        ],
    },
    {
        "char": "よ",
        "words": [
            {"word": "よっつ", "emoji": "4️⃣", "keyword_en": "four"},
            {"word": "よる", "emoji": "🌙", "keyword_en": "night"},
            {"word": "よこ", "emoji": "↔️", "keyword_en": "horizontal"},
        ],
    },
    # ら行
    {
        "char": "ら",
        "words": [
            {"word": "らいおん", "emoji": "🦁", "keyword_en": "lion"},
            {"word": "らっぱ", "emoji": "🎺", "keyword_en": "trumpet"},
            {"word": "らくだ", "emoji": "🐪", "keyword_en": "camel"},
        ],
    },
    {
        "char": "り",
        "words": [
            {"word": "りんご", "emoji": "🍎", "keyword_en": "apple"},
            {"word": "りす", "emoji": "🐿️", "keyword_en": "squirrel"},
            {"word": "りぼん", "emoji": "🎀", "keyword_en": "ribbon"},
        ],
    },
    {
        "char": "る",
        "words": [
            {"word": "るびー", "emoji": "💎", "keyword_en": "ruby"},
            {"word": "るすばん", "emoji": "🏠", "keyword_en": "house sitting"},
            {"word": "るーれっと", "emoji": "🎡", "keyword_en": "roulette"},
        ],
    },
    {
        "char": "れ",
        "words": [
            {"word": "れもん", "emoji": "🍋", "keyword_en": "lemon"},
            {"word": "れいぞうこ", "emoji": "🧊", "keyword_en": "refrigerator"},
            {"word": "れっしゃ", "emoji": "🚂", "keyword_en": "train"},
        ],
    },
    {
        "char": "ろ",
        "words": [
            {"word": "ろうそく", "emoji": "🕯️", "keyword_en": "candle"},
            {"word": "ろけっと", "emoji": "🚀", "keyword_en": "rocket"},
            {"word": "ろば", "emoji": "🫏", "keyword_en": "donkey"},
        ],
    },
    # わ行
    {
        "char": "わ",
        "words": [
            {"word": "わに", "emoji": "🐊", "keyword_en": "crocodile"},
            {"word": "わし", "emoji": "🦅", "keyword_en": "eagle"},
            {"word": "わっか", "emoji": "⭕", "keyword_en": "ring circle"},
        ],
    },
    {
        "char": "を",
        "words": [
            {"word": "をどり", "emoji": "💃", "keyword_en": "dance"},
            {"word": "をかし", "emoji": "🤣", "keyword_en": "funny"},
            {"word": "をとこ", "emoji": "👦", "keyword_en": "boy"},
        ],
    },
    # ん
    {
        "char": "ん",
        "words": [
            {"word": "んごろごろ（ねこ）", "emoji": "😸", "keyword_en": "purring cat"},
            {"word": "ぱんだ", "emoji": "🐼", "keyword_en": "panda"},
            {"word": "りんご", "emoji": "🍎", "keyword_en": "apple"},
        ],
    },
]

# 行ごとのグループ定義（親モードのフィルタ用）
HIRAGANA_GROUPS: dict[str, list[str]] = {
    "あ行": ["あ", "い", "う", "え", "お"],
    "か行": ["か", "き", "く", "け", "こ"],
    "さ行": ["さ", "し", "す", "せ", "そ"],
    "た行": ["た", "ち", "つ", "て", "と"],
    "な行": ["な", "に", "ぬ", "ね", "の"],
    "は行": ["は", "ひ", "ふ", "へ", "ほ"],
    "ま行": ["ま", "み", "む", "め", "も"],
    "や行": ["や", "ゆ", "よ"],
    "ら行": ["ら", "り", "る", "れ", "ろ"],
    "わ行": ["わ", "を", "ん"],
}

# 文字から単語データを引くための辞書に変換
HIRAGANA_DICT: dict[str, dict] = {item["char"]: item for item in HIRAGANA_DATA}
