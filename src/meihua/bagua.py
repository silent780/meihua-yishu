"""
八卦与六十四卦的定义
"""


class Hexagram:
    """六十四卦的定义与属性"""
    
    # 八卦符号
    BAGUA = {
        "乾": [1, 1, 1],  # 天
        "兑": [1, 1, 0],  # 泽
        "离": [1, 0, 1],  # 火
        "震": [1, 0, 0],  # 雷
        "巽": [0, 1, 1],  # 风
        "坎": [0, 1, 0],  # 水
        "艮": [0, 0, 1],  # 山
        "坤": [0, 0, 0],  # 地
    }
    
    # 六十四卦定义
    HEXAGRAMS = {
        "乾乾": {
            "name": "乾为天",
            "text": "元亨利贞。",
            "explanation": "大吉大利，占问得此卦，前程光明，心想事成。刚健笃实，自强不息。"
        },
        "坤坤": {
            "name": "坤为地",
            "text": "元亨，利牝马之贞。",
            "explanation": "地势坤，君子以厚德载物。包容万物，适合稳健发展。"
        },
        "震震": {
            "name": "震为雷",
            "text": "亨。震来虩虩，笑言哑哑。震惊百里，不丧匕鬯。",
            "explanation": "震动变化，有惊无险。行动要谨慎，变革中保持警觉。"
        },
        "艮艮": {
            "name": "艮为山",
            "text": "艮其背，不获其身，行其庭，不见其人，无咎。",
            "explanation": "适时止住，懂得节制。静观其变，不盲目行动。"
        },
        "坎坎": {
            "name": "坎为水",
            "text": "习坎，有孚，维心亨，行有尚。",
            "explanation": "险中求通，谨慎前行。处于困境中，保持诚信和坚定的意志。"
        },
        "离离": {
            "name": "离为火",
            "text": "利贞，亨。畜牝牛，吉。",
            "explanation": "光明显耀，内心澄明。坚守正道，大事可成。"
        },
        "巽巽": {
            "name": "巽为风",
            "text": "小亨，利有攸往，利见大人。",
            "explanation": "谦和顺从，循序渐进。随势而动，寻求贵人指点。"
        },
        "兑兑": {
            "name": "兑为泽",
            "text": "亨，利贞。",
            "explanation": "喜悦和谐，心情愉快。坚持正确方向，保持乐观态度。"
        },
        "乾坤": {
            "name": "天地否",
            "text": "否之匪人，不利君子贞，大往小来。",
            "explanation": "天地不交，阴阳不通。困难时期，宜守不宜进。"
        },
        "坤乾": {
            "name": "地天泰",
            "text": "小往大来，吉亨。",
            "explanation": "天地交泰，阴阳和谐。大吉大利，诸事顺遂。"
        },
        "乾震": {
            "name": "天雷无妄",
            "text": "无妄，元亨利贞。其匪正有眚，不利有攸往。",
            "explanation": "无妄之灾，无心之失。行动须谨慎，不可妄为。"
        },
        "震乾": {
            "name": "雷天大壮",
            "text": "大壮，利贞。",
            "explanation": "刚强盛壮，志在必得。正大光明，勇往直前。"
        },
        "乾艮": {
            "name": "天山遁",
            "text": "遁，亨，小利贞。",
            "explanation": "暂时退避，蓄势待发。韬光养晦，伺机而动。"
        },
        "艮乾": {
            "name": "山天大畜",
            "text": "利贞，不家食吉，利涉大川。",
            "explanation": "蓄养德行，厚积薄发。储备实力，以待时机。"
        },
        "乾坎": {
            "name": "天水讼",
            "text": "有孚窒惕，中吉，终凶。利见大人，不利涉大川。",
            "explanation": "争讼不断，纷争难解。寻求调解，避免激化。"
        },
        "坎乾": {
            "name": "水天需",
            "text": "有孚，光亨，贞吉。利涉大川。",
            "explanation": "等待时机，不可强求。耐心期待，水到渠成。"
        },
        "乾离": {
            "name": "天火同人",
            "text": "同人于野，亨。利涉大川，利君子贞。",
            "explanation": "志同道合，同心协力。团结一致，事业可成。"
        },
        "离乾": {
            "name": "火天大有",
            "text": "元亨。",
            "explanation": "丰盛昌盛，前途光明。拥有资源，事业发达。"
        },
        "乾巽": {
            "name": "天风姤",
            "text": "女壮，勿用取女。",
            "explanation": "阴长阳消，变化之始。谨防小人，守正防变。"
        },
        "巽乾": {
            "name": "风天小畜",
            "text": "亨。密云不雨，自我西郊。",
            "explanation": "蓄养小善，逐渐积累。涵养德行，待时而动。"
        },
        "乾兑": {
            "name": "天泽履",
            "text": "履虎尾，不咥人，亨。",
            "explanation": "谨慎行事，如履薄冰。持守正道，稳中求进。"
        },
        "兑乾": {
            "name": "泽天夬",
            "text": "扬于王庭，孚号有厉。告自邑，不利即戎，利有攸往。",
            "explanation": "决断明确，排除障碍。坚定前行，果断处理。"
        },
        "坤震": {
            "name": "地雷复",
            "text": "亨。出入无疾，朋来无咎。反复其道，七日来复，利有攸往。",
            "explanation": "阳气初生，生机复苏。东山再起，否极泰来。"
        },
        "震坤": {
            "name": "雷地豫",
            "text": "利建侯行师。",
            "explanation": "喜悦欢欣，顺遂安乐。保持谦和，适度享受。"
        },
        "坤艮": {
            "name": "地山谦",
            "text": "亨，君子有终。",
            "explanation": "谦虚谨慎，自我约束。功成不居，德行日增。"
        },
        "艮坤": {
            "name": "山地剥",
            "text": "不利有攸往。",
            "explanation": "剥落衰退，日渐消亡。处变不惊，等待时机。"
        },
        "坤坎": {
            "name": "地水师",
            "text": "贞丈人吉，无咎。",
            "explanation": "统御众人，团结一致。有序行进，循序渐进。"
        },
        "坎坤": {
            "name": "水地比",
            "text": "吉。原筮，元永贞，无咎。不宁方来，后夫凶。",
            "explanation": "亲密和睦，团结互助。同心协力，诚信相待。"
        },
        "坤离": {
            "name": "地火明夷",
            "text": "利艰贞。",
            "explanation": "内明外晦，韬光养晦。处于困境，保持光明。"
        },
        "离坤": {
            "name": "火地晋",
            "text": "康侯用锡马蕃庶，昼日三接。",
            "explanation": "上进发展，稳步前行。循序渐进，步步高升。"
        },
        "坤巽": {
            "name": "地风升",
            "text": "元亨，用见大人，勿恤，南征吉。",
            "explanation": "上行向上，逐渐提升。奋发向上，循序渐进。"
        },
        "巽坤": {
            "name": "风地观",
            "text": "盥而不荐，有孚颙若。",
            "explanation": "观察大势，明辨是非。审时度势，见微知著。"
        },
        "坤兑": {
            "name": "地泽临",
            "text": "元亨利贞，至于八月有凶。",
            "explanation": "临近监督，关怀体恤。明察秋毫，公正处事。"
        },
        "兑坤": {
            "name": "泽地萃",
            "text": "亨，王假有庙，利见大人，亨，利贞。用大牲吉，利有攸往。",
            "explanation": "会聚团结，众志成城。集合力量，共同前进。"
        },
        "震艮": {
            "name": "雷山小过",
            "text": "亨，利贞，可小事，不可大事。飞鸟遗之音，不宜上，宜下，大吉。",
            "explanation": "小有越轨，无伤大体。谨慎行事，不可贪大。"
        },
        "艮震": {
            "name": "山雷颐",
            "text": "贞吉。观颐，自求口实。",
            "explanation": "养身养性，滋养生命。慎言节食，修身养性。"
        },
        "震坎": {
            "name": "雷水解",
            "text": "利西南，无所往，其来复吉。有攸往，夙吉。",
            "explanation": "解除困难，排解纷争。解除束缚，柳暗花明。"
        },
        "坎震": {
            "name": "水雷屯",
            "text": "元亨利贞，勿用有攸往，利建侯。",
            "explanation": "初始困难，坚持到底。创业艰难，守正不阿。"
        },
        "震离": {
            "name": "雷火丰",
            "text": "亨。王假之，勿忧，宜日中。",
            "explanation": "丰盛充实，盛大辉煌。适度享受，不可奢侈。"
        },
        "离震": {
            "name": "火雷噬嗑",
            "text": "亨。利用狱。",
            "explanation": "咬合相连，明辨是非。严明执法，公正处理。"
        },
        "震巽": {
            "name": "雷风恒",
            "text": "亨，无咎，利贞，利有攸往。",
            "explanation": "持之以恒，坚定不移。长久之道，贵在坚持。"
        },
        "巽震": {
            "name": "风雷益",
            "text": "利有攸往，利涉大川。",
            "explanation": "有所增益，获得好处。积极进取，勇于冒险。"
        },
        "震兑": {
            "name": "雷泽归妹",
            "text": "征凶，无攸利。",
            "explanation": "女子归嫁，结束一段。谨守本分，安分守己。"
        },
        "兑震": {
            "name": "泽雷随",
            "text": "元亨利贞，无咎。",
            "explanation": "随顺变化，顺势而为。柔顺谦和，随机应变。"
        },
        "艮坎": {
            "name": "山水蒙",
            "text": "亨。匪我求童蒙，童蒙求我。初筮告，再三渎，渎则不告。利贞。",
            "explanation": "启蒙教育，开导蒙昧。循序渐进，教学相长。"
        },
        "坎艮": {
            "name": "水山蹇",
            "text": "利西南，不利东北，利见大人，贞吉。",
            "explanation": "行走艰难，进退维谷。坚韧不拔，终将通达。"
        },
        "艮离": {
            "name": "山火贲",
            "text": "亨。小利有攸往。",
            "explanation": "文饰修美，注重外表。适度装饰，不可过度。"
        },
        "离艮": {
            "name": "火山旅",
            "text": "小亨，旅贞吉。",
            "explanation": "旅途在外，暂时停留。谨慎行事，不可久留。"
        },
        "艮巽": {
            "name": "山风蛊",
            "text": "元亨，利涉大川，先甲三日，后甲三日。",
            "explanation": "整治混乱，革除积弊。大刀阔斧，改革创新。"
        },
        "巽艮": {
            "name": "风山渐",
            "text": "女归吉，利贞。",
            "explanation": "渐进发展，循序渐进。稳扎稳打，水到渠成。"
        },
        "艮兑": {
            "name": "山泽损",
            "text": "有孚，元吉，无咎，可贞，利有攸往。曷之用，二簋可用享。",
            "explanation": "有所损失，必有所得。适当减损，获得平衡。"
        },
        "兑艮": {
            "name": "泽山咸",
            "text": "亨，利贞，取女吉。",
            "explanation": "相互感应，情投意合。柔顺相待，和谐共处。"
        },
        "坎离": {
            "name": "水火既济",
            "text": "亨，小利贞，初吉终乱。",
            "explanation": "事业完成，功成名就。保持警惕，防止败落。"
        },
        "离坎": {
            "name": "火水未济",
            "text": "亨，小狐汔济，濡其尾，无攸利。",
            "explanation": "尚未完成，继续努力。谨慎前行，防止失败。"
        },
        "坎巽": {
            "name": "水风井",
            "text": "改邑不改井，无丧无得，往来井井。汔至，亦未繘井，羸其瓶，凶。",
            "explanation": "源源不断，滋养万物。守正不阿，利济天下。"
        },
        "巽坎": {
            "name": "风水涣",
            "text": "亨，王假有庙，利涉大川，利贞。",
            "explanation": "分散涣散，疏通阻滞。化解困境，开拓前路。"
        },
        "坎兑": {
            "name": "水泽节",
            "text": "亨，苦节不可贞。",
            "explanation": "节制调节，适度平衡。取舍有度，进退有节。"
        },
        "兑坎": {
            "name": "泽水困",
            "text": "亨，贞，大人吉，无咎，有言不信。",
            "explanation": "身陷困境，内外受限。坚持不懈，终将脱困。"
        },
        "离巽": {
            "name": "火风鼎",
            "text": "元吉，亨。",
            "explanation": "革故鼎新，更新变化。承前启后，继往开来。"
        },
        "巽离": {
            "name": "风火家人",
            "text": "利女贞。",
            "explanation": "家庭和睦，内外有别。各安其位，和谐共处。"
        },
        "离兑": {
            "name": "火泽睽",
            "text": "小事吉。",
            "explanation": "背道而驰，互不相容。求同存异，和而不同。"
        },
        "兑离": {
            "name": "泽火革",
            "text": "巳日乃孚，元亨利贞，悔亡。",
            "explanation": "革除旧弊，更新变革。适时而变，顺势而为。"
        },
        "巽兑": {
            "name": "风泽中孚",
            "text": "豚鱼吉，利涉大川，利贞。",
            "explanation": "诚信笃实，言行一致。诚实守信，坦诚相待。"
        },
        "兑巽": {
            "name": "泽风大过",
            "text": "栋桡，利有攸往，亨。",
            "explanation": "过度失衡，超出常规。谨慎行事，防止失控。"
        }
    }
    
    def __init__(self, upper_trigram, lower_trigram):
        """
        初始化一个卦象
        :param upper_trigram: 上卦名称
        :param lower_trigram: 下卦名称
        """
        self.upper = upper_trigram
        self.lower = lower_trigram
        self.key = upper_trigram + lower_trigram  # 总是连接两个卦名
        
        # 获取卦象信息
        hexagram_info = self.HEXAGRAMS.get(self.key, {"name": "未知卦象", "text": "", "explanation": ""})
        self.name = hexagram_info["name"]
        self.text = hexagram_info["text"]
        self.explanation = hexagram_info["explanation"]
    
    @classmethod
    def from_yao_list(cls, yao_list):
        """从爻列表创建卦象"""
        if len(yao_list) != 6:
            raise ValueError("爻列表必须包含6个爻")
        
        # 解析上卦和下卦（下卦为初爻到三爻，上卦为四爻到六爻）
        lower_values = [yao.value for yao in yao_list[0:3]]
        upper_values = [yao.value for yao in yao_list[3:6]]
        
        # 查找对应的八卦名称
        upper_trigram = None
        lower_trigram = None
        
        for name, values in cls.BAGUA.items():
            if values == upper_values:
                upper_trigram = name
            if values == lower_values:
                lower_trigram = name
        
        if not upper_trigram or not lower_trigram:
            raise ValueError("无法识别的卦象")
        
        return cls(upper_trigram, lower_trigram)
    
if __name__ == "__main__":
    # 测试八卦卦象
    from yao import Yao
    yao_list = [Yao.random() for _ in range(6)]
    print(yao for yao in yao_list)
    hexagram = Hexagram.from_yao_list(yao_list)
    print(f"卦象：{hexagram.name}")
    print(f"卦辞：{hexagram.text}")
    print(f"解释：{hexagram.explanation}")

