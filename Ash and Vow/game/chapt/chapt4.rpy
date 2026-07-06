
# ==================== 第四章入口（承接第三章正常通关结局） ====================
label chapter_four_start:
    scene bg hermit_hut with dissolve:
        vp
    play bgm bgm_hermit_warm fadeout 1.0 fadein 2.0
    play sound soft_campfire loop
    show char old_man at center:
        zoom(0.4)

    # 强制显示双主角立绘
    show isold_normal at left:
        zoom(2.0)
    show karen_normal at right:
        zoom(0.4)


    narrator "黑雾笼罩的枯林深处，破败石砌隐士小屋内壁刻满淡蓝色烬火传承咒文，火光将三人影子拉长投在冰冷石墙上。隐士铺开一卷泛黄兽皮古籍，符文泛出幽幽冷光。"

    old_man "(指尖摩挲兽皮上褪色的双血脉纹路，语气沉重肃穆)"
    old_man "你们二人是现存仅有的两支纯血烬火。百年前族群分裂，一部分族人贪图力量与黯蚀魔物缔结盟约，便是如今的黯蚀骑士教会；剩余遗脉四散流亡，我隐居此地，只为等候纯血继承者到来。"

    karen "(指尖死死扣住武士刀刀柄，眼底翻涌浓烈恨意，无任何过往回忆台词)"
    karen "屠灭我部族的叛徒，只是骑士统领的棋子，他真正效忠的人是谁？"

    old_man "王城大教堂的大主教。祭坛溃败的消息早已传入王城，叛徒携带完整全域献祭法阵图纸藏匿在大教堂地下密室。一旦仪式完成，整片大陆都会被黯蚀黑雾彻底吞噬。"

    narrator "你下意识抬起左臂，腕间烬火印记骤然发烫，冰蓝色微光顺着手臂肌肤流淌，淡金色古老西幻咒文缓缓浮现浮动。"
    show effect mark_glow with flash
    pause 2.0
    hide effect arm_rune_blue

    isold "我的血脉力量每次全力爆发，都会被黑雾侵蚀心神，这份缺陷该如何弥补？"

    old_man "有两条路稳固你的血脉根基。其一，随我静心调息，循序渐进解锁传承，稳妥无致命风险；其二，前往后山黑石血脉祭坛，以自身魔力为引强行淬炼力量，短期战力暴涨，但稍有不慎就会被黯蚀吞噬理智。"

    stop soft_campfire
    play sound march_armor loop
    narrator "屋外传来成片重甲踏步轰鸣，浓稠黑雾瞬间包裹整片林地，数十名高阶黯蚀骑士包围石屋。身披暗紫鎏金战甲的黑刃骑士队长从雾中缓步走出，杀气扑面而来。"
    show char black_knight_cap at center:
        zoom(0.15)
        yoffset 200

    black_knight_cap "(隔着黑雾放声冷笑，金属盔甲震颤作响)"
    black_knight_cap "大主教传令，活捉两名烬火纯血，敢反抗者当场抹杀！"

    stop march_armor
    play sound boss_clash loop
    narrator "隐士抬手撑起一层淡蓝色火焰屏障隔绝黑雾，转头看向你们二人，语气急促。"

    old_man "我来牵制屋外杂兵，你们立刻做出抉择：进山淬炼血脉稳固力量，或是正面杀出重围直奔王城！"
    hide char black_knight_cap
    hide char old_man

    # 战斗力分层判定，解锁三大主线分支
    menu:
        "前往后山黑石祭坛，强行淬炼烬火血脉"if combat_power >= 56:
            jump branch_a_blood_altar
        "跟随隐士静心调息，温和解锁血脉传承"if combat_power >= 40 and combat_power <= 55:
            jump branch_b_meditate_train
        "暂避锋芒，前往西境寻找烬火遗民求援"if combat_power < 40:
            jump branch_c_find_allies

# ==============================================================================
# 主线A：后山祭坛淬炼血脉 combat_power >= 56
# 子分支：A1高好感 / A2中好感 / A3低好感
# ==============================================================================
label branch_a_blood_altar:
    scene bg blood_altar_mountain with dissolve
    show char isold_normal at left
    show char karen_normal at right:
        zoom(0.1)
    play bgm bgm_boss_fight fadeout 1.0 fadein 2.0

    narrator "荒芜黑石山道四周漂浮腐蚀黑雾，伊索尔德见你执意踏入危险祭坛淬炼血脉，毫不犹豫提刀跟在你身侧，全程寸步不离。"

    karen "淬炼仪式风险极高，我不会让你独自面对黯蚀侵蚀，有任何异变我会立刻出手支援。"

    narrator "二人抵达刻满上古咒文的圆形血脉祭坛，你催动冰蓝色烬火自掌心蔓延全身，伊索尔德同时释放粉紫色斩魔焰，两道火焰在空中缠绕交融，触发双人合击特效。"
    show effect ember_combine with flash
    pause 2.2
    hide effect ember_combine

    narrator "淬炼中途，地底涌出大量浓稠黯蚀黑雾疯狂钻进你的经脉，剧痛席卷全身，意识濒临失控。伊索尔德快步上前紧紧攥住你的手臂，双血脉之力共鸣，泪珠顺着脸颊滑落，眼窝浮起清冷闪光粒子。"
    show effect tear_glow with flash
    pause 1.8
    hide effect tear_glow

    karen "(语气坚定，无过往回忆，仅诉说当下羁绊)"
    karen "你是如今唯一能与我并肩对抗教会的人，我不能眼睁睁看你被黑暗吞噬。"

    menu:
        "合力击溃骑士队长，获取王城密道情报"if trust_isol >= 60:
            jump c4_a1_trust_high
        "各自运转力量完成淬炼，联手清理敌军"if trust_isol >= 30 and trust_isol < 60:
            jump c4_a2_trust_mid
        "二人爆发争吵，伊索尔德留守小屋抗敌":
            jump a3_trust_low

# A1 高好感完美通关线
label c4_a1_trust_high:
    scene bg hermit_stone_hut with dissolve:
        vp
    show char isold_normal at left
    show char karen_normal at right:
        zoom(0.4)
    show char black_knight_cap at center

    narrator "淬炼完成后二人血脉力量同步暴涨，折返石屋合力围剿黑刃骑士队长，一番死战将其斩杀。从队长尸身搜出叛徒写给大主教的密信，记录大教堂地下潜入密道。"
    hide char black_knight_cap

    old_man "(将一枚蓝宝石烬火圣物递到你手中)"
    old_man "你们二人的羁绊足以驾驭纯血力量，这枚传承吊坠能压制黯蚀侵蚀，前往王城时带上。"

    $ combat_power += 15
    $ trust_isol += 20

    scene bg dead_forest_path with dissolve:
        vp
    show char isold_normal at left
    show char karen_normal at right
    play sound soft_campfire loop

    narrator "林间空地燃起篝火，二人整理密信情报规划王城行动路线。伊索尔德与你定下约定，抵达大教堂先解决叛徒，再联手阻止全域献祭仪式。"
    narrator "【第四章分支A1 双焰共生·传承结局完成，解锁第五章王城双人潜行主线，双人合击技能永久升级】"
    jump end_all

# A2 中好感普通战友线
label c4_a2_trust_mid:
    scene bg hermit_stone_hut with dissolve:
        vp
    show char isold_normal at left
    show char karen_normal at right
    show char black_knight_cap at center

    narrator "淬炼全程二人各自运转血脉力量，火焰没有产生共鸣联动，仪式平稳完成。二人合力斩杀黑刃骑士队长，拿到王城密道线索。伊索尔德全程只谈论追杀叛徒的战术，无私人情绪倾诉。"
    hide char black_knight_cap

    $ combat_power += 12
    $ trust_isol += 9

    narrator "二人简单休整后动身前往王城，赶路途中极少交谈，彼此仅保持战友协作关系。"
    narrator "【第四章分支A2 烈焰同行·战友结局完成，正常开启第五章标准主线，无专属双人CG】"
    jump end_all

# A3 低好感分歧分支（双选择：克制成功 / 力量失控坏结局）
label c4_a3_trust_low:
    scene bg blood_altar_mountain with dissolve
    show char isold_normal at left
    show char karen_normal at right

    narrator "伊索尔德强烈反对你选择高风险淬炼仪式，认为盲目追求力量会走上叛徒的老路，二人爆发激烈争执。她拒绝陪同进山，独自返回石屋协助隐士抵御骑士杂兵，你孤身踏入黑石祭坛。"

    menu:
        "咬紧牙关克制黯蚀心魔，成功完成淬炼，立刻赶回石屋支援":
            jump c4_a3_save_success
        "淬炼时被黯蚀支配心智，出手袭击赶来寻你的伊索尔德":
            jump a3_badend_lose_blood

label c4_a3_save_success:
    scene bg hermit_stone_hut with dissolve:
        vp
    show char isold_normal at left
    show char karen_normal at right
    show char black_knight_cap at center

    narrator "你强忍黑雾侵蚀完成血脉淬炼，浑身布满腐蚀伤痕赶回石屋，独自斩杀黑刃骑士队长。伊索尔德看见你重伤模样，内心生出一丝动摇，隔阂略微消减。"
    hide char black_knight_cap
    $ combat_power += 6
    $ trust_isol += 5

    narrator "二人勉强达成共识结伴前往王城，全程气氛冰冷，几乎没有交流。"
    narrator "【第四章分支A3 烈焰裂痕·隔阂结局完成，解锁第五章疏离同行支线】"
    jump end_one

label a3_badend_lose_blood:
    scene bg fog_forest_battle with dissolve:
        vp
    show char isold_normal at center
    hide char karen_normal
    play bgm bgm_sad_break fadein 1.0

    narrator "黯蚀黑雾彻底吞噬你的意识，你失控冲向前来寻找你的伊索尔德，隐士立刻出手用火焰屏障隔开二人。伊索尔德对你彻底失望，独自动身追踪叛徒踪迹，不再与你同行。"
    narrator "【坏结局：血脉失序，第四章强制中断，仅解锁第五章单人独行支线，无法触发双人剧情】"
    jump end_one

# ==============================================================================
# 主线B：静心调息温和传承 40 ≤ combat_power ≤55
# 子分支：B1高好感 / B2中好感 / B3低好感
# ==============================================================================
label branch_b_meditate_train:
    scene bg hermit_stone_hut with dissolve:
        vp
    show char isold_normal at left
    show char karen_normal at right
    play bgm bgm_stealth_quiet fadeout 1.0 fadein 2.0

    narrator "二人每日在后院石台跟随隐士调息修炼，专注学习稳定烬火血脉的法门。修炼时你手臂印记频繁发烫，冰蓝闪光与金色咒文不断浮现。"
    show effect arm_rune_blue at isold_normal with flash
    pause 1.5
    hide effect arm_rune_blue

    menu:
        "【高好感B1 林间低语·羁绊结局】默契配合修炼，潜行绕开骑士主力撤离林地"if trust_isol >= 60:
            jump c4_b1_trust_high
        "【中好感B2 稳步前行·同伴结局】分工破解符文机关，收集骑士教会情报"if trust_isol >= 30 and trust_isol < 60:
            jump c4_b2_trust_mid
        "【低好感B3 信任隔阂·分道分支】伊索尔德嫌修炼拖沓，催促立刻动身追杀叛徒":
            jump c4_b3_trust_low

# B1 高好感温情潜行线
label c4_b1_trust_high:
    scene bg dead_forest_path with dissolve:
        vp
    show char isold_normal at left
    show char karen_normal at right

    narrator "二人熟练掌握血脉调息之法，隐士交付林间密道地图，依靠潜行规避大批骑士巡逻队，只解决落单零散士兵，沿路收集大量教会献祭罪证密卷。夜晚露宿山洞，二人全程只交流对抗大主教的战术规划。"

    $ combat_power += 8
    $ trust_isol += 16

    narrator "【第四章分支B1 林间低语·心动潜行结局完成，解锁第五章双人潜入大教堂专属支线，双人调息CG解锁】"
    jump end_all

# B2 中好感平稳同伴线
label c4_b2_trust_mid:
    scene bg hermit_stone_hut with dissolve:
        vp
    show char isold_normal at left
    show char karen_normal at right

    narrator "二人分工破解石壁上古符文机关，各自处理沿途魔物与巡逻骑士，顺利拿到林间密道路线。约定抵达王城后分工行动，你牵制卫兵，她搜寻叛徒下落，全程无深度私下交谈。"

    $ combat_power += 5
    $ trust_isol += 8

    narrator "【第四章分支B2 稳步前行·同伴结局完成，正常开启第五章主线】"
    jump end_all

# B3 低好感分歧选择
label c4_b3_trust_low:
    scene bg dead_forest_path with dissolve:
        vp
    show char isold_normal at left
    show char karen_normal at right

    narrator "伊索尔德认为静心修炼太过耽误追杀叛徒的时机，数次催促你放弃调息直接动身，二人矛盾持续激化。"

    menu:
        "坚持完成全套血脉修炼，修炼结束后独自追赶提前离开的伊索尔德":
            jump b3_save_reconcile
        "妥协放弃修炼，立刻动身直奔王城，力量不足遭遇骑士伏击":
            jump b3_badend_ambush

label b3_save_reconcile:
    scene bg fog_forest_battle with dissolve:
        vp
    show char isold_normal at left
    show char karen_normal at right

    narrator "你完成修炼后立刻沿密道追赶伊索尔德，半路撞见她被骑士小队围困，你出手将敌军击溃。伊索尔德态度略微软化，勉强结伴同行前往王城。"
    $ trust_isol += 5
    narrator "【第四章分支B3 半路和解·疏离结局完成，解锁第五章短暂分道支线】"
    return

label b3_badend_ambush:
    scene bg fog_forest_battle with dissolve
    show char isold_normal at center:
        zoom(1.6)
    hide char karen_normal
    play bgm bgm_sad_break fadein 1.0

    narrator "二人未稳固血脉力量仓促上路，中途撞上大批高阶黯蚀骑士伏击。伊索尔德为掩护你身受重创，暂时失去行动能力，只能你独自继续追查叛徒踪迹。"
    narrator "【坏结局：密林伏击，第四章强制中断，第五章无女主同行剧情】"
    jump end_one

# ==============================================================================
# 主线C：暂避锋芒寻找烬火遗民 combat_power < 40
# 子分支：C1高好感 / C2中好感 / C3低好感双坏结局
# ==============================================================================
label branch_c_find_allies:
    scene bg dead_forest_path with dissolve:
        vp
    show char isold_normal at left:
        zoom(0.4)
    show char karen_normal at right:
        zoom(0.4)
    play bgm bgm_solemn fadeout 1.0 fadein 2.0

    narrator "你体内烬火力量根基薄弱，无法支撑淬炼或长时间正面作战。隐士提议前往西境残存烬火遗民据点求援，集结族人力量再反攻王城。"

    menu:
        "结伴穿越废墟抵达遗民据点，获得援军支援"if trust_isol >= 60:
            jump c4_c1_trust_high
        "顺利抵达据点，原地休整等待援军集结"if trust_isol >= 30 and trust_isol < 60:
            jump c4_c2_trust_mid
        "伊索尔德拒绝等待援军，在岔路爆发决裂争吵":
            jump c4_c3_trust_low

# C1 低战力完美援军线
label c4_c1_trust_high:
    scene bg abandon_castle_ruin with dissolve:
        vp
    show char isold_normal at left
    show char karen_normal at right

    narrator "赶路途中伊索尔德全程主动掩护你避开魔物与骑士巡逻，每当你手臂烬火印记失控发烫，她便手把手教你快速压制力量的技巧。二人穿过废弃古堡废墟，平安抵达西境烬火遗民据点。"

    narrator "遗民看见你们双份纯血脉印记，愿意集结全部残存战士，一同前往王城阻止大主教全域献祭仪式。"
    $ combat_power += 4
    $ trust_isol += 22

    narrator "【第四章分支C1 遗脉同心·援军完美结局完成，第五章解锁多人联手作战剧情，战斗难度大幅降低】"
    return

# C2 低战力平稳休整线
label c4_c2_trust_mid:
    scene bg abandon_castle_ruin with dissolve:
        vp
    show char isold_normal at left
    show char karen_normal at right

    narrator "二人顺利抵达烬火遗民据点，族人应允出兵支援，你们原地休整数日打磨基础血脉力量，等待援军全部集结完毕再向王城进发。赶路途中二人仅交换路线、敌情信息，无额外私人交谈。"
    $ combat_power += 2
    $ trust_isol += 6

    narrator "【第四章分支C2 借兵休整·平稳结局完成，正常开启第五章主线】"
    jump end_all

# C3 低好感双坏结局分支
label c4_c3_trust_low:
    scene bg dead_forest_path with dissolve:
        vp
    show char isold_normal at left
    show char karen_normal at right:
        zoom(0.4)
    play bgm bgm_sad_break fadein 1.0

    narrator "伊索尔德无法接受继续拖延复仇进度，在前往西境据点的林间岔路与你爆发终极争吵，两条道路都会触发第四章坏结局，无法完整开启第五章主线。"

    menu:
        "坚持前往遗民据点寻求援军，劝说伊索尔德冷静等待":
            jump c3_badend_capture_karen
        "妥协顺从伊索尔德，二人直接孤身奔赴王城大教堂":
            jump c3_badend_all_capture

label c3_badend_capture_karen:
    scene bg fog_forest_battle with dissolve:
        vp
    show char isold_normal at left
    hide char karen_normal

    narrator "你执意前往西境求援，伊索尔德一气之下独自折返骑士包围圈追杀叛徒，寡不敌众被生擒囚禁。你只能独自前往遗民据点集结兵力，后续单人营救。"
    narrator "【坏结局：黑雾囚笼2，第四章中断，第五章女主长期被俘，无双人同行剧情】"
    return

label c3_badend_all_capture:
    scene bg fog_forest_battle with dissolve:
        vp
    show char isold_normal at left
    show char karen_normal at right:
        zoom(0.4)

    narrator "二人力量不足以对抗王城外围大批高阶黯蚀骑士，半路被敌军层层包围，锁链捆缚押往大教堂地下密室，等候大主教开启献祭仪式。"
    narrator "【坏结局：大主教祭品，第四章阶段性强制通关，游戏进入单人营救特殊支线】"
    return