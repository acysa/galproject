

# ==================== 第三章入口跳转（承接第二章结尾） ====================
label chapter_three_start:
    scene bg forest_road with dissolve: 
        vp
    play bgm bgm_solemn fadeout 1.5
    play sound footstep1 loop

    # 强制显示双主角立绘，左右分位，全程保留
    show char karen_normal at right
    show char isold_normal at left

    narrator "穿过幽影之森层层叠叠的黑雾密林，你们顺着祭坛石壁上遗留的暗紫色符文线索，一路向着林地最深处前行。林间的黯蚀气息越来越厚重，腕间的烬火印记持续发烫，仿佛在预警前方藏着足以吞噬一切的黑暗源头。"

    karen "(指尖轻轻按住腰间武士刀刀柄，紫调眼瞳望向深处翻涌的浓雾，语气压着一层藏不住的恨意)"
    karen "石壁上的符文格式，和我部族古籍里记载的献祭法阵完全一致。当年屠戮我族人的骑士，正是依靠这种仪式汲取黯蚀力量。走到底，我们就能找到所有阴谋的答案。"

    $ trust_isol_temp = trust_isol
    $ combat_temp = combat_power

    isold "一路走来，我能清晰感觉到黑雾里的恶意。不管前方等待我们的是骑士军团还是魔物，我都会和你一同面对。"

    narrator "两人并肩持续向前行走了近半个时辰，脚下泥土渐渐变得潮湿黏腻，空气中混杂着铁锈、腐烂草木与阴冷魔力的刺鼻气味。前方山体裂开一道巨大的洞窟入口，浓稠的黑色雾气源源不断从洞口涌出，低频的嗡鸣声从洞窟深处缓缓传来，震得耳膜微微发麻。"

    stop footstep1
    play sound altar_hum loop
    scene bg altar_cave with fade:
        vp
    # 切换场景后重新加载双人立绘，不消失
    show char karen_normal at right
    show char isold_normal at left
    play bgm bgm_altar_tension fadein 2.0

    narrator "踏入地下祭坛洞窟的瞬间，视线瞬间被无边无际的黑雾包裹。两侧数十米高的岩壁上，密密麻麻刻满了千年以来的献祭记录，每一道刻痕都记载着被抓捕的血脉继承者如何沦为黯蚀能量的养料。无数残破的镣铐、干涸的血迹附着在石壁之上，随处可见当年受难者遗留的零碎衣物。"

    karen "(脚步停顿，伸手抚上岩壁一道古老刻痕，指尖微微发颤，尘封的部族回忆不受控制翻涌而出)"
    karen "这道纹路……是我幼时守护我的长老留下的。当年屠村之时，他为了掩护我逃跑，被骑士生擒带到此处献祭。这么多年，我一直不敢细想他最后的遭遇。"

    isold "(主动往她身侧靠近半步，抬手轻轻覆在她的手背，温和安抚)"
    isold "都过去了。今天我们来到这里，就是为了终结这一切，不会再有人重蹈覆辙。"

    narrator "就在二人沉浸在沉重的过往心绪中时，洞窟深处传来沉重的锁链拖拽声响，断断续续的虚弱咳嗽声顺着黑雾飘来。伊索尔德瞬间握紧武士刀，眼神瞬间从悲伤转为警惕，二人放轻脚步，循着声响往洞窟内侧摸索。"
    play sound chain_drag loop

    # 加载长老NPC立绘，双主角依旧保留画面两侧
    show char old_man at center:
        zoom(0.4)
    narrator "绕过一排断裂的石柱，你们看见一名白发枯瘦老者被厚重玄铁锁链捆缚在石壁之上，衣衫破损，皮肤布满黯蚀腐蚀的黑斑。老者听见脚步声，费力抬起头，浑浊的双眼落在伊索尔德身上时，骤然睁大，满是难以置信。"

    old_man "(气息虚弱，声音沙哑破碎)"
    old_man "那抹红紫渐变的长发……是烬火遗族最后的血脉，当年侥幸逃生的孩子，你居然活到了现在。"

    karen "(瞳孔震颤，长刀垂落半分，难掩震惊)"
    karen "您认识我？您是当年部族的守典长老？"

    old_man "正是。当年部族覆灭根本不是骑士单方面突袭，族内出了叛徒，提前将我们的藏身之地、血脉之力的弱点全部出卖给了黯蚀统领。我被活捉至此囚禁数十年，每日被迫记录献祭法阵的运转规律，见证骑士一步步扩张黑暗势力。"

    narrator "长老缓缓道出祭坛的核心秘密，洞窟最深处的黑暗核心是整片幽影之森黑雾的本源，骑士统领正筹备一场大规模献祭仪式，一旦仪式完成，他们便能彻底掌控黯蚀能量，向外扩张征服整片大陆。他给你们指明两条可行的破局路线，同时给出第三条稳妥退路。"

    old_man "想要终止仪式，有三条路可选。第一条，正面从洞窟正门冲杀祭坛核心，凭借力量强行击碎黑暗本源，适合力量雄厚之人；第二条，走侧面隐藏暗道潜行，悄悄切断献祭符文法阵，从根源削弱核心，不需要硬抗主力骑士；第三条，若是自身力量不足以应对危机，暂时放弃摧毁核心，前往森林深处隐士的居所寻求外援，沉淀力量后再折返。"

    old_man "孩子，你们自行抉择前路，我会将我所知的所有骑士部署线索全部告知你们。"

    stop chain_drag
    stop altar_hum
    hide char old_man # 长老退场，男女主仍保留画面

    narrator "长老将一卷泛黄的兽皮地图塞到你们手中，地图上清晰标注了三条路线的分布、骑士巡逻点位与陷阱位置。此刻系统判定你的综合战力，解锁对应可选路线。"

    # ========== 战斗力分层判定，解锁主线分支菜单 ==========
    menu:
        "【高强战力】正面强攻祭坛核心，与骑士军团正面决战" if combat_power >= 56:
            jump branch_a_attack_front
        "【标准战力】走隐秘暗道潜行，切断献祭法阵" if combat_power >= 40 and combat_power <= 55:
            jump branch_b_stealth_tunnel
        "【战力不足】暂时退避，前往隐士居所寻找援助" if combat_power < 40:
            jump branch_c_escape_hermit

# ======================================================================================
# 主线分支A：高强战力正面强攻路线 combat_power >=56
# 内部依据 trust_isol 好感分为 A1高好感 / A2中好感 / A3低好感
# ======================================================================================
label branch_a_attack_front:
    scene bg altar_boss_arena with dissolve:
        vp
    # 切换战斗场景，立刻加载双主角立绘
    show char karen_normal at right
    show char isold_normal at left
    play bgm bgm_boss_fight fadeout 1.0 fadein 2.0
    play sound march_armor loop

    narrator "你选择正面硬闯祭坛核心，握紧掌心瞬间催动烬火之力，鎏金火焰顺着腕间纹路蔓延至整条手臂，温热的力量充盈四肢百骸。伊索尔德见状上前与你并肩站立，武士刀刀身浮现一层淡紫色焰光，与你的金色火焰遥遥呼应。"

    karen "(目光落在你周身流转的烬火，若是好感足够会流露柔软，反之语气紧绷)"
    if trust_isol >= 60:
        karen "我从未想过，有一天能有人与我并肩直面这份宿命。这么多年孤身复仇的恐惧，在见到你的火焰时，终于消散大半。"
        narrator "伊索尔德主动伸手握住你的手腕，二人近距离对视，眼底盛满隐忍的温柔与多年积攒的心酸，眼眶慢慢泛起水光，触发含情对视落泪CG分镜场景。"
        show effect tear_glow at karen_normal with flash
        pause 1.8
        show effect tear_glow at isold_normal with flash
        pause 1.5
    elif trust_isol >= 30 and trust_isol < 60:
        karen "你的力量足够支撑我们冲破防线，我们分工配合，你压制魔物，我斩杀骑士士兵，不要擅自脱离配合阵型。"
    else:
        karen "你太过莽撞，正面军团人数众多，稍有失误我们都会葬身此处。若是开战中途一意孤行，我不会分心救你。"

    narrator "洞窟前方的开阔决战场地，数十名精英黯蚀骑士整齐列阵，身披加厚黑雾甲胄，手持附魔长矛。队伍最前方，身披暗金重甲的骑士统领缓步走出，周身环绕浓稠的腐蚀黑雾，气息威压远超路上遭遇的所有敌人。"

    narrator "大战瞬间爆发，成片骑士一拥而上。伊索尔德身形化作红紫残影，武士刀每一次劈砍都带起撕裂黑雾的焰风；你催动全身烬火，金色烈焰屏障挡下所有远程长矛攻击，火焰飞刃成片横扫杂兵。当统领携带着致命黯蚀重击冲向你时，伊索尔德毫不犹豫横刀挡在你的身前。"

    play sound boss_clash loop
    show effect ember_combine at center with flash

    narrator "危急关头，二人力量本能交融，解锁专属合击技「烬火紫焰斩」，金紫双色火焰交织成巨型刃光，横扫整片战场，普通骑士尽数被击溃消散，只剩骑士统领独自站立。一番持久恶战后，统领护甲开裂，力量大幅衰弱。"
    stop boss_clash

    menu:
        "【高好感羁绊结局A1】合力斩杀统领，揪出部族叛徒，摧毁黑暗核心" if trust_isol >= 60:
            jump a1_trust_high
        "【中好感战友结局A2】击杀统领，叛徒趁乱逃脱，摧毁核心暂时平息黑雾"if trust_isol >= 30 and trust_isol < 60:
            jump a2_trust_mid
        "【低好感分歧分支A3】伊索尔德独自突进陷入重围，立刻做出救援选择" if trush_isol <30:
            jump a3_trust_low

# A1 高好感完美结局
label a1_trust_high:
    # 全程保留双人立绘
    show char karen_normal at right
    show char isold_normal at left
    narrator "双人合击重创统领后，伊索尔德一眼认出统领身侧躲在黑雾里的侍从，那人胸前佩戴的部族纹饰，正是当年出卖全族的叛徒。你主动牵制重伤的统领，伊索尔德持刀上前，了结埋藏数十年的仇恨。"

    narrator "心结彻底解开，二人一同踏入祭坛核心房间，联手以烬火紫焰击碎涌动黑雾的黑暗本源。整片幽影之森的黑雾以肉眼可见的速度消散，洞窟内压抑的阴冷气息一扫而空。"
    $ combat_power += 10
    $ trust_isol += 15

    scene bg forest_hideout with dissolve:
        vp
    show char karen_normal at right
    show char isold_normal at left
    play bgm bgm_hide_quiet fadeout 1.0 fadein 2.0
    play sound soft_campfire loop

    narrator "夜幕降临，二人寻到林间避风空地点燃篝火。火光映亮伊索尔德泛红的眼尾，她直白道出长久以来藏在心底的心意，约定往后一同游走大陆，寻找幸存的烬火血脉遗民，再也不分开。"

    narrator "【第三章分支A1 焰光同归·羁绊真结局完成，解锁第四章双人专属同行剧情】"
    jump chapter_four_start

# A2 中好感普通战友结局
label a2_trust_mid:
    show char karen_normal at right
    show char isold_normal at left
    narrator "你与伊索尔德合力击溃骑士统领，但混乱的战场之中，当年出卖部族的叛徒趁黑雾掩护偷偷从侧门逃窜，消失在密林深处，留下后续追查伏笔。二人无暇追击，优先冲进核心洞窟击碎黑暗本源，暂时压制整片森林的黯蚀黑雾。"

    $ combat_power += 7
    $ trust_isol += 8

    narrator "危机暂时解除，二人简单休整，伊索尔德依旧沉浸在未能手刃叛徒的遗憾之中，全程只和你交流线索与前路规划，没有流露私人情感，维持纯粹战友关系。二人商议先前往隐士据点整理收集到的阴谋证据，再追查叛徒踪迹。"

    narrator "【第三章分支A2 烈焰并肩·战友结局完成，正常开启第四章主线】"
    jump chapter_four_start

# A3 低好感分歧分支，救援二选一
label a3_trust_low:
    show char karen_normal at right
    show char isold_normal at left
    narrator "因为彼此信任不足，开战前的争吵影响配合，伊索尔德不愿等待你的支援，独自持刀冲向统领，瞬间被数道黯蚀锁链缠住四肢，深陷重围，黑雾不断侵蚀她的躯体，情况危急。你必须立刻做出选择。"

    menu:
        "不顾一切冲上前耗尽力量救援伊索尔德":
            jump a3_save_success
        "优先自保，独自突围逃离祭坛":
            jump a3_save_fail_badend

label a3_save_success:
    show char karen_normal at right
    show char isold_normal at left
    narrator "你不顾一切催动体内全部烬火，无视自身经脉灼烧的剧痛，冲破骑士包围圈，火焰屏障护住被束缚的伊索尔德，斩断黯蚀锁链。脱困后的她看着你苍白疲惫的模样，心底生出浓烈愧疚，对过往的固执产生动摇。"

    narrator "二人勉强联手击溃统领，摧毁黑暗核心，但伊索尔德全程沉默寡言，休整结束后坦言需要独自消化仇恨与愧疚，暂时离队，第四章开启单人独行支线。"
    $ combat_power += 6
    $ trust_isol += 5
    narrator "【第三章分支A3 烈焰裂痕·隔阂结局完成，解锁单人特殊支线】"
    return  ####需要补充单人线

label a3_save_fail_badend:
    scene bg altar_cave with dissolve:
        vp
    # 仅保留男主立绘，女主被俘消失
    show char isold_normal at center
    hide char karen_normal
    play bgm bgm_sad_break fadein 1.0
    narrator "你选择独自抽身突围，丢下被困的伊索尔德往洞窟出口狂奔。身后传来她被骑士制服的闷响与压抑的呼喊，黑雾彻底吞没她的身影。你不敢回头，一路疯狂冲出地下祭坛，孤身一人逃入幽影之森外围。"
    narrator "伊索尔德被骑士生擒囚禁，沦为献祭备选祭品，本章剧情强制中断，无法解锁第四章主线，触发坏结局【祭坛囚笼】，仅可读取存档重选分支。"
    scene bg end_4:
        vp

# ======================================================================================
# 主线分支B：标准战力潜行路线 40 ≤ combat_power ≤55
# 内部依据 trust_isol 好感分为 B1高好感 / B2中好感 / B3低好感
# ======================================================================================
label branch_b_stealth_tunnel:
    scene bg secret_tunnel with dissolve:
        vp
    show char karen_normal at right
    show char isold_normal at left
    play bgm bgm_stealth_quiet fadeout 1.0 fadein 2.0
    play sound stealth_step loop

    narrator "你们听从长老建议，顺着地图标记找到祭坛侧边隐藏的狭窄暗道，通道岩壁布满遮挡视线的藤蔓，仅容两人贴身并行。全程需要压低身形，避开每隔十步一轮的骑士巡逻小队，一旦暴露就会被大批骑士包围。"

    karen "(放轻脚步紧贴你的身侧，气息压到最低，根据好感度触发不同对话)"
    if trust_isol >= 60:
        karen "我年少逃亡时，无数次躲在这种狭小缝隙躲避追兵，那时身边空无一人，只能独自熬过分分秒秒。如今身旁有你，连潜藏的黑暗都不再让人恐惧。"
        narrator "二人躲在石缝规避巡逻骑士，距离近到呼吸交织，安静的暗道里只有彼此的心跳声，伊索尔德侧头看向你，眼底满是藏不住的心动，轻声说起幼年独自躲藏追兵的完整回忆。"
    elif trust_isol >= 30 and trust_isol < 60:
        karen "我们分头留意左右两侧的巡逻动静，你负责用烬火微光破解机关符文，我处理落单魔物，发现敌情立刻互通信号。"
    else:
        karen "不要随意触碰通道内的符文机关，你的控力不稳很容易触发警报，若是暴露行踪，我不会停下潜行计划等你。"

    narrator "沿路零星游荡低阶黯蚀魔物阻拦前路，你依靠平稳凝练的烬火之力悄无声息解决，伊索尔德则用短刀斩断阻挡通路的锁链与法阵连接线。一路配合抵达献祭法阵中枢，只需要切断四根核心符文锁链，就能大幅削弱黑暗核心的力量。"

    menu:
        "【高好感默契结局B1】双人配合切断全部符文，悄悄解救长老一同撤离森林" if trust_isol >= 60:
            jump b1_trust_high
        "【中好感平稳结局B2】分头破解机关，顺利切断法阵，独自撤离前往隐士据点" if trust_isol >= 30 and trust_isol < 60:
            jump b2_trust_mid
        "【低好感分歧分支B3】伊索尔德擅自行动触发巡逻警报，立刻选择掩护或独自逃跑" if trust_isol <30:
            jump b3_trust_low

# B1 高好感潜行完美结局
label b1_trust_high:
    show char karen_normal at right
    show char isold_normal at left
    narrator "二人默契配合，你以温和烬火激活符文锁，伊索尔德精准斩断法阵锁链，四根核心符文全部失效，祭坛深处的黑暗核心瞬间黯淡，骑士军团因法阵崩溃陷入大面积混乱。趁着全场骚乱，你们折返囚禁长老的石壁，解开玄铁锁链将老者搀扶带走。"

    narrator "三人顺着暗道原路撤离幽影之森，抵达森林外围安全地带后，长老将部族失传的血脉静心心法传授给你们。路上伊索尔德不断和你分享年少漂泊独行的细碎往事，二人羁绊持续加深。"
    $ combat_power += 6
    $ trust_isol += 12

    narrator "【第三章分支B1 暗影密行·心动结局完成，正常开启第四章主线，解锁双人调息专属剧情】"
    jump chapter_four_start

# B2 中好感潜行普通结局
label b2_trust_mid:
    show char karen_normal at right
    show char isold_normal at left
    narrator "你们分头行动破解两侧机关，各自清理沿途拦路魔物，顺利切断献祭法阵锁链。但二人没有多余心力折返解救长老，只能趁着骑士混乱独自从暗道逃离，约定后续提升实力再折返营救老者。"

    $ combat_power += 4
    $ trust_isol += 6

    narrator "离开幽影之森后，二人径直前往隐士据点休整，整理收集到的祭坛符文碎片与骑士密信，全程只交流线索与生存规划，没有深入的私人谈心桥段，同伴关系平稳无升温。"
    narrator "【第三章分支B2 暗阵脱身·同行结局完成，正常开启第四章主线】"
    jump chapter_four_start

# B3 低好感潜行分歧分支
label b3_trust_low:
    show char karen_normal at right
    show char isold_normal at left
    narrator "伊索尔德不信任你的控力判断，不等你同步信号就独自上前触碰符文机关，机关瞬间迸发刺眼黑雾警报，整片暗道响起骑士集结的号角声，大批重甲骑士朝着暗道合围而来，眼下仅有两个选择。"

    menu:
        "主动站在前方释放烬火掩护伊索尔德从密道先撤离":
            jump b3_cover_success
        "放弃等待，独自从侧边小型密道先行逃跑":
            jump b3_cover_fail_badend

label b3_cover_success:
    show char karen_normal at right
    show char isold_normal at left
    narrator "你撑开大范围火焰屏障独自阻拦涌来的骑士，硬扛数道黯蚀长矛攻击，身受轻伤，硬生生拖出足够时间让伊索尔德顺着窄缝撤离。待追兵被火焰牵制，你才找机会绕路逃出祭坛。"

    narrator "二人在森林外围约定的汇合点重逢，伊索尔德看着你身上的伤口，内心生出浓重愧疚，一路返程途中主动减少强硬言语，但依旧存在隔阂，第四章剧情短暂分道而行。"
    $ combat_power += 3
    $ trust_isol += 4
    narrator "【第三章分支B3 潜行愧疚·疏离结局完成，解锁短暂分道支线】"
    jump chapter_four_start

label b3_cover_fail_badend:
    scene bg secret_tunnel with dissolve:
        vp
    show char isold_normal at center
    hide char karen_normal
    play bgm bgm_sad_break fadein 1.0
    narrator "你选择抛弃伊索尔德独自逃进侧边狭窄密道，身后传来她被骑士包围的兵刃碰撞声与压抑的呼喊。你头也不回冲出暗道，孤身一人逃进密林深处，伊索尔德被骑士俘虏囚禁，触发坏结局【迷雾囚禁】，本章强制结束，无法开启第四章主线。"
    scene end_3

# ======================================================================================
# 主线分支C：低战力迂回避战路线 combat_power <40
# 内部依据 trust_isol 好感分为 C1高好感 / C2中好感 / C3低好感（无正常通关，双坏结局）
# ======================================================================================
label branch_c_escape_hermit:
    scene bg altar_cave with dissolve:
        vp
    show char karen_normal at right
    show char isold_normal at left
    play bgm bgm_altar_tension fadein 1.0
    narrator "你清晰感知自身当前力量尚且薄弱，贸然正面交战或是潜行切断法阵都极易出现失误，听从长老提议暂时放弃摧毁黑暗核心，先动身前往森林深处隐士的居所寻求外援，沉淀力量后再折返祭坛清算骑士阴谋。"

    karen "(观察到你眼底的无力，根据好感度切换情绪态度)"
    if trust_isol >= 60:
        karen "力量强弱从来不是衡量胜负的唯一标准，懂得审时度势保全自身，才是长久走下去的关键。我不会因为你暂时无法对抗骑士而失望，我们一同去找隐士修炼，等你血脉之力沉淀扎实，我们再回来了结一切。"
        narrator "伊索尔德主动拉着你走到洞窟外侧干净石台，坐下引导你静心调息，手把手教你平稳引导烬火流转的法门，漫长谈心过程中，完整讲述部族典籍记载的上古血脉传说。"
    elif trust_isol >= 30 and trust_isol < 60:
        karen "暂且避战是稳妥选择，我们收集祭坛内所有阴谋证据，抵达隐士居所寻求支援，待力量提升后再重返祭坛。"
    else:
        karen "一味逃避解决不了仇恨，我被困在数十年的痛苦之中，根本无法再继续等待。我无法认同你退缩的选择。"

    narrator "二人收起长老交付的兽皮地图，顺着森林外围安全路线避开所有骑士巡逻点，沿路收集骑士密信、腐蚀符文碎片等关键物证，一路向着隐士隐居的林间小屋前行。"

    menu:
        "【高好感温情结局C1】安稳抵达隐士居所，获得修炼指导与援助承诺" if trust_isol >= 60:
            jump c1_trust_high
        "【中好感休整结局C2】顺利抵达据点，约定后续重返祭坛清算" if trust_isol >= 30 and trust_isol < 60:
            jump c2_trust_mid
        "【低好感决裂分支C3】伊索尔德因避战选择爆发争吵，做出路线抉择" if trust_isol < 30:
            jump c3_trust_low

# C1 低战力完美温情结局
label c1_trust_high:
    scene bg hermit_hut with dissolve:
        vp
    show char karen_normal at right
    show char isold_normal at left
    play bgm bgm_hermit_warm fadeout 1.0 fadein 2.0
    play sound soft_campfire loop

    narrator "二人一路相互扶持，平安抵达隐蔽的林间隐士小屋。白发隐士看过你们带来的祭坛证据与血脉印记，知晓黯蚀骑士的滔天阴谋，承诺待你们完成血脉修炼，便调动隐居的残存血脉修士一同重返幽影之森摧毁黑暗核心。"

    narrator "往后数日你们留在隐士居所静心修炼，伊索尔德每日陪你调息打磨烬火之力，二人无数个夜晚围坐篝火畅谈过往与未来，羁绊大幅加深，解锁第四章专属双人修炼主线剧情。"
    $ combat_power += 3
    $ trust_isol += 18

    narrator "【第三章分支C1 林间静修·温情结局完成，正常开启第四章最优主线】"
    jump chapter_four_start

# C2 低战力普通休整结局
label c2_trust_mid:
    scene bg hermit_hut with dissolve:
        vp
    show char karen_normal at right
    show char isold_normal at left
    play bgm bgm_hermit_warm fadeout 1.0

    narrator "你们顺利抵达隐士居所，将收集到的全部祭坛物证交付隐士。隐士应允待你们力量足够后提供支援，二人短暂休整数日，每日各自单独打磨力量，仅在规划前路时简单交谈，无深度情感互动。"
    $ combat_power += 2
    $ trust_isol += 7

    narrator "二人约定沉淀足够战力后，立刻折返幽影之森摧毁黑暗核心、营救囚禁的长老。"
    narrator "【第三章分支C2 暂避迷雾·休整结局完成，正常开启第四章主线】"
    jump chapter_four_start

# C3 低好感决裂双坏结局分支
label c3_trust_low:
    scene bg forest_road with dissolve:
        vp
    show char karen_normal at right
    show char isold_normal at left
    play bgm bgm_sad_break fadein 1.0
    narrator "还未走到隐士居所，伊索尔德便因你选择逃避复仇彻底爆发争吵，多年积压的痛苦与执念让她无法接受暂时退让，两条道路摆在眼前，无论如何选择都无法打出正常通关结局。"

    menu:
        "坚持前往隐士居所寻求援助，劝说伊索尔德冷静":
            jump c3_choose_hermit_badend
        "妥协顺从伊索尔德，折返祭坛强行对抗骑士军团":
            jump c3_choose_altar_badend

label c3_choose_hermit_badend:
    scene bg forest_road with dissolve:
        vp
    show char isold_normal at left
    hide char karen_normal
    narrator "你执意前往隐士据点，伊索尔德在林间岔路与你彻底决裂，独自转身折返黑雾祭坛，孤身一人持武士刀冲击骑士主力军团。数日后你从隐士口中得知，伊索尔德寡不敌众，血染祭坛，永久离世触发结局【血染祭坛】"
    scene bg end_1:
        vp

label c3_choose_altar_badend:
    scene bg altar_cave with dissolve:
        vp
    show char karen_normal at right
    show char isold_normal at left
    narrator "你不忍伊索尔德独自赴死，妥协跟随她折返地下祭坛。你的战力完全不足以抗衡骑士军团，二人联手依旧节节败退，最终双双被骑士生擒，锁链捆缚送往黑暗核心完成献祭仪式，触发阶段性全灭坏结局【献祭轮回】，游戏阶段性结束。"
    scene bg end_2:
        vp