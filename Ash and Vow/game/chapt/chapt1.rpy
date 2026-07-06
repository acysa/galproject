

# ======================================================
# 分支一：trust_father = 1 林间密道与追踪者
# ======================================================
label route_1:
    scene bg tunnel_dark:
        vp
    play bgm bgm_tunnel fadeout 1.0 fadein 2.0
    play sound footstep loop

    hide char marcus_normal
    show char karen_normal at left
    show char isold_normal at right:
        zoom(1.4)
        yoffset -280

    narrator "地窖的木门在身后闭合，将镇内的厮杀与喧嚣彻底隔绝。狭长的密道昏暗潮湿，墙面刻满古老符文。伊索尔德举着火折子，火光在通道里轻轻摇曳。"

    isold "这条密道是早年镇民为躲避战乱开凿的，知晓的人寥寥无几。神父愿意把铜徽交给你，足以证明他百分百信任你。"
    karen "这枚徽章……究竟有什么用处？"

    isold "它可以压制你手腕印记散发出的血脉气息。黯蚀骑士依靠波动追踪目标，有它遮蔽，短期内我们不会被大范围锁定。但效果有限，必须尽快离开这片林区。"
    karen "他们不惜屠戮村落，就为了追捕拥有这道印记的人？"

    isold "(脚步微顿，神色凝重)"
    isold "不止于此。黯蚀骑士团痴迷禁忌的黯蚀之力，传言你的血脉，是唤醒旧日力量的关键。边境接连被毁的村落，全是他们搜寻遗脉留下的痕迹。"

    narrator "二人低声交谈，脚步不曾停歇。通道尽头，渐渐吹来了林间的冷风与淅沥雨声。"
    pause 1.0

    scene bg rain_forest with fade:
        vp
    play bgm bgm_forest fadeout 1.0 fadein 2.0
    stop footstep
    play sound rain loop

    narrator "走出密道，冰冷的雨水再次打湿衣衫。密林间雾气弥漫，能见度极低，整片森林安静得令人心慌。"
    isold "这里太静了，斥候大概率已经进山。跟紧我，千万不要走散。"
    karen "我明白。"

    narrator "二人压低身形，在参天古木间快速穿行。不多时，前方传来了金属碰撞与人声低语。"
    play sound whisper
    hide char karen_normal
    hide char isold_normal

    scene bg forest_clearing with fade:
        vp
    narrator "两名黑甲斥候正沿路搜查，甲胄缝隙间萦绕着诡异黑雾，正是追杀你们的黯蚀骑士。"

    narrator "【斥候甲】上头下令，找到那名带血脉印记的少年，活要见人，死也要带回躯体。"
    narrator "【斥候乙】整片林子都被封锁了，他插翅难飞。"

    show char isold_normal at right:
        zoom(1.4)
        yoffset -280        
    isold "(拔出短刀，压低声音)"
    isold "只有两个人。我上前牵制，你趁机绕路先走，我随后就追上你。"

    narrator "话音未落，伊索尔德纵身跃出，短刀直刺对方破绽。两名斥候立刻举盾格挡，缠斗瞬间爆发。"
    play sound fight loop
    show char isold_normal at center:
        zoom(2.4)
        yoffset -100

    narrator "黑甲武士力量凶悍，黑雾所触之处草木迅速枯萎。伊索尔德身手灵活，以一敌二渐渐落入下风，肩头被盾沿磕碰，脚步踉跄。"

    show char karen_normal at left:
        zoom(0.2)
        yoffset -278
        xzoom(-1.0)
    karen "(心头一紧，失声呼喊)"
    karen "小心！"

    show effect mark_glow with dissolve
    pause 1.5
    hide effect mark_glow
    stop fight

    narrator "情绪激荡的瞬间，你的左手腕骤然发烫，淡金色光芒骤然炸开。一股强劲的无形力量席卷全场，两名斥候被狠狠震退，甲胄上的黑雾也短暂消散。"
    narrator "对方面露惊惧，一时不敢上前。"

    isold "(怔怔看向你，满眼震惊)"
    isold "这股力量……实在太过特殊。"

    isold "(立刻回神，上前拉住你的手臂)"
    isold "快走！力量波动会引来更多追兵！"
    play sound retreat loop

    narrator "二人不敢停留，转身向着密林深处狂奔。力量褪去后，你只觉得四肢发软，显然这份力量的使用并非毫无代价。"
    pause 1.0

    scene bg hunter_hut with fade:
        vp
    play bgm bgm_hut_safe fadeout 1.0 fadein 2.0
    stop retreat
    stop rain

    narrator "一路奔逃，你们最终躲进森林深处一间废弃的猎人小屋。紧绷的神经终于得以放松。"
    show char karen_normal at left:
        zoom(0.4)
        yoffset -278
        xzoom(-1.0)
    show isold_normal warm at right:
        zoom(0.4)
        yoffset 0

    isold "(靠在门板上喘息，看向你的目光多了明显的认可)"
    $ trust_isol += 1

    isold "刚才爆发的力量，就是你血脉里的能力吗？远比我想象中强大。"
    karen "我根本无法主动掌控它，情绪一激动就会自行苏醒。而且使用过后，身体会格外疲惫。"

    isold "(眉头微蹙，认真分析局势)"
    isold "你的力量，暂时冲破了铜徽的遮蔽。如今整片森林都被骑士团封锁，前后路口皆有重兵把守。"
    isold "现在我们有两个选择，你决定接下来的路线。"

    menu:
        "等到深夜浓雾变浓，从西侧陡坡突围":
            $ combat_power+=3
            jump choice_breakout
        "深入森林腹地，寻找流浪者据点暂避":
            jump choice_hideout

label choice_breakout:
    narrator "你决定趁深夜浓雾最盛之时，从西侧陡坡强行突围。"
    isold "陡坡地势险峻，骑士布防薄弱，但山路湿滑危险。做好准备，等到夜色最深我们就动身。"
    narrator "屋外雨声未歇，隐约传来远处的马蹄声。危机仍在步步逼近。"
    narrator "【第一章：林间密道与追踪者 · 章节结束】"
    jump chapter2_main_line
    

label choice_hideout:
    narrator "你选择继续深入雨林，前往传闻中的流浪者据点躲避风头。"
    isold "森林深处人迹罕至，相对安全，但路途遥远，还可能遭遇野兽。事不宜迟，我们现在就出发。"
    narrator "小屋的木门再次被推开，二人踏入更深、更未知的密林之中。"
    narrator "【第一章：林间密道与追踪者 · 章节结束】"
    return

# ======================================================
# 分支二：trust_father = 0 霜鸦镇的秘密
# ======================================================
label route_2:
    scene bg church_hall_dawn:
        vp
    play bgm bgm_dawn_quiet fadeout 1.0 fadein 2.0

    narrator "你放弃了密道逃亡，选择留在霜鸦镇探查真相。雨夜渐渐停歇，天边泛起鱼肚白，整座小镇陷入一种诡异的平静。马库斯神父对你戒备未消，没有赠予任何护身物件，态度疏离冷淡。"

    show char karen_normal at left
    show char isold_normal at right

    isold "你真的要留在镇上？黯蚀骑士的目标明确，留在这里无异于置身险境。"
    karen "一味逃跑解决不了问题。神父明明知晓内情，却闭口不谈，还有追杀我的人……我必须弄清楚一切。"

    show char marcus_normal at center:
        zoom(0.4)
    marcus "(低头擦拭烛台，语气淡漠)"
    marcus "知道越多，灾祸缠身。你刻意隐瞒过往，我自然不会多言。好自为之。"

    narrator "说完，马库斯转身走向教堂后方，刻意回避所有交谈。"
    hide char marcus_normal

    isold "(无奈叹气)"
    isold "他性子谨慎，既然不信任你，便不会吐露秘密。但眼下最大的隐患，是镇里的内奸。边境小镇人迹罕至，骑士团能精准赶来，必然有人通风报信。"
    karen "内奸？"
    isold "没错。我们分头走访街巷、商铺，收集线索，天黑前在这里汇合。"
    karen "好，彼此小心。"

    scene bg town_street_day with fade:
        vp
    play bgm bgm_town_suspense fadeout 1.0 fadein 2.0
    play sound crowd_murmur loop

    narrator "白日的霜鸦镇看似正常营业，可每当你走过街巷，居民们都会下意识侧目，目光落在你的手腕处，躲闪、畏惧、忌惮交织在一起。铁匠、酒馆老板、路边行人，所有人都在刻意回避与你交谈。"
    pause 2.0

    narrator "半日探查结束，你与伊索尔德准时汇合，交换各自打探到的消息。二人配合默契，慢慢拼凑出线索，隔阂也渐渐消散。"
    $ trust_isol += 1

    show char karen_normal at left:
        zoom(0.4)
        yoffset -278
    show char isold_normal at right:
        zoom(1.2)
        yoffset -280
    isold "我打听到，昨夜骑士抵达前，镇外出现过陌生人影。而且居民们统一回避‘印记’‘旧神’相关话题，明显是被人叮嘱过。"
    karen "这里的人，似乎从一开始就知道我的存在。他们在共同守护一个秘密。"

    isold "疑点越来越多。我们暂时没有证据，不能贸然指认他人。先返回教堂，等到入夜再继续观察。"

    scene bg church_courtyard with fade:
        vp
    play bgm bgm_night_tension fadeout 1.0 fadein 2.0
    stop crowd_murmur

    narrator "夕阳西下，暮色笼罩小镇。家家户户早早紧闭门窗，街巷彻底变得冷清。"
    show char marcus_normal at right:
        zoom(0.4)
    marcus "(路过庭院，语气带着警告)"
    marcus "入夜之后，不要踏出教堂半步。今晚，镇子不会太平。"

    karen "您明明知道真相，为什么不肯告诉我们？"
    marcus "我守护小镇的秘密，是为了保全所有人。你来历不明，我不敢冒险。"

    narrator "马库斯不再回应，径直离开。"
    hide char marcus_normal

    isold "别再多问了。提高警惕，危险恐怕很快就会降临。"

    scene bg town_outside_night with fade:
        vp
    narrator "深夜来临，你和伊索尔德守在钟楼眺望远方。忽然，镇外西侧荒地上，一团漆黑的火焰猛地窜上夜空。"
    play sound signal_fire
    narrator "那是内奸发出的联络信号！"

    isold "(神色大变)"
    isold "不好！骑士团要行动了！"

    play sound knight_rush loop
    narrator "震天的马蹄声、甲胄碰撞声从四面八方袭来。大批黯蚀骑士冲破小镇围栏，黑雾席卷街巷，居民的惊呼声此起彼伏。"

    narrator "没时间追查内奸，伊索尔德立刻拉着你冲出教堂，借着房屋掩护在街巷中狂奔。"
    play sound retreat loop

    narrator "镇上居民紧闭门窗，无人出手相助，只是默默旁观。你们一路躲避搜捕，奋力冲向小镇后方的出口。"
    pause 2.0

    scene bg wildroad_cross with fade:
        vp
    stop knight_rush
    stop retreat
    stop signal_fire

    narrator "终于，二人冲出小镇边界，站在了茫茫荒野的岔路口。身后的追捕声依旧清晰，前路摆在眼前。"
    show char karen_normal at left
    show char isold_normal at right

    isold "内奸的身份、小镇的秘密，我们只能暂时搁置。现在选择接下来的方向吧。"

    menu:
        "沿官道前行，前往远方城镇休整，探寻身世":
            jump route2_choice_town
        "走偏僻野路迂回，伺机折返查清小镇真相":
            jump route2_choice_back

label route2_choice_town:
    narrator "你决定踏上宽阔官道，前往远方的城镇。远离这片边境是非之地，一边休整，一边继续追查自己血脉与身世的真相。"
    narrator "【第一章：霜鸦镇的秘密 · 章节结束】"
    jump chapter2_main_line

label route2_choice_back:
    narrator "你不愿就此放弃疑点，选择走入偏僻荒野小路。打算绕路迂回，等待时机再返回霜鸦镇，揭穿内奸、挖出小镇隐藏的秘密。"
    narrator "【第一章：霜鸦镇的秘密 · 章节结束】"
    jump chapter2_detour_line

# ======================================================
# 分支三：留下抵挡 → 初次觉醒 · 结伴上路（完整版扩充剧情）
# ======================================================
label route_3:
    scene bg town_gate_dark:
        vp
    play bgm bgm_danger fadeout 1.0 fadein 2.0
    play sound knight_rush loop

    narrator "你执意留下阻拦追兵，伊索尔德短暂犹豫后，放弃撤离，握紧短刀选择与你并肩作战。夜色漆黑，雨水打湿地面，一支黯蚀骑士小队已经完成合围。甲胄缝隙中不断溢出灰黑色雾气，所过之处杂草尽数枯萎。马库斯站在教堂门廊下，神色凝重地注视着战场。"

    show char karen_normal at left
    show char isold_normal at right:
        zoom(1.4)
        yoffset -280

    narrator "为首的黑甲骑士上前一步，头盔下传出沙哑冰冷的嗓音。"
    narrator "交出拥有旧神印记的遗脉，饶你们不死。负隅顽抗，只会一同化为黑雾。"

    isold "(侧身挡在你身前，姿态紧绷)"
    isold "想带走他，先踏过我的尸体。这些被黯蚀之力侵蚀的怪物，我早已见惯。"

    karen "(轻轻拉开伊索尔德，迈步向前)"
    karen "我不会跟你们走。你们屠戮村落、追捕无辜之人，恶行到此为止吧。"

    narrator "你手腕的印记开始微微发烫，能清晰感受到对方身上的邪恶力量，正在与自己的血脉产生诡异呼应。为首骑士一声冷哼，抬手下令进攻。战斗正式打响。"
    play sound fight loop
    $ combat_power+=10

    narrator "伊索尔德身法灵动，短刀专挑铠甲缝隙、关节等弱点进攻。可骑士身披重甲，又被黯蚀之力强化，防御力惊人，黑雾还在持续侵蚀人的体力与精神。几番交手后，人数劣势逐渐显现。"

    narrator "一名骑士绕至侧面，挥舞铁盾狠狠撞向伊索尔德。她躲闪不及，被盾沿击中腰腹，闷哼着踉跄后退，短刀险些脱手。黑色雾气顺着伤口蔓延而上。"
    hide char isold_normal
    show char isold_normal at right:
        zoom(1.4)
        yoffset -280
    isold "(强忍痛楚，气息不稳)"
    isold "别管我……他们目标是你，趁机快走！"

    narrator "骑士们抓住空档，集体向你合围而来。刺骨的杀意笼罩全身，死亡危机近在眼前。看着受伤的伊索尔德，你的情绪彻底爆发，体内的血脉力量被完全唤醒。"

    karen "(咬牙低喝)"
    karen "到此为止了！"

    show effect mark_glow with dissolve
    pause 1.8
    hide effect mark_glow
    stop fight
    stop knight_rush

    narrator "手腕上的印记骤然亮起刺目金光，滚烫的热流顺着血管流遍全身。金色火焰萦绕周身，磅礴的旧神力量轰然炸开。迎面而来的骑士被气浪狠狠掀飞，身上的黯蚀黑雾遇火消融。"
    narrator "全场陷入死寂，骑士们连连后退，满眼忌惮。"

    narrator "可狂暴的力量在体内横冲直撞，经脉阵阵刺痛，眩晕感袭来。你勉强稳住身形，周身火光微微黯淡。"
    karen "(低声喘息)"
    karen "这股力量……我还无法完全掌控。"

    narrator "为首骑士看出你状态不稳，厉声下令准备二次冲锋。就在此时，马库斯快步走出，高举一枚刻满古老符文的木牌。"
    show char marcus_normal at center:
        zoom(0.4)
        yoffset 278
    play sound magic_barrier

    marcus "此地是旧神守护者的领地，尔等休得放肆！"

    narrator "柔和的白光展开一道屏障，暂时挡住了骑士的脚步，双方陷入僵持。"
    marcus "(看向你，语气严肃又带着期许)"
    marcus "你的力量已经彻底暴露，整片边境的黯蚀势力都会疯狂追查你。霜鸦镇，再也留不住你了。"

    narrator "他取出一卷泛黄的羊皮纸递到你手中。"
    marcus "这上面标记了一处隐士据点，那里有人通晓旧神历史，能教导你掌控力量。沿着森林主路向东前行即可。记住，力量是守护的依仗，绝非杀戮的工具。"

    karen "多谢神父提点，这份恩情我不会忘记。"

    isold "(揉了揉腰侧伤口，目光无比坚定)"
    isold "你尚不熟悉自身力量，骑士又诡计多端，我不能让你独自上路。我陪你一起。"
    $ trust_isol += 2

    narrator "骑士持续冲击屏障，木牌光芒越来越微弱，支撑不了多久。你们不再逗留，转身朝着后山森林奔去。"
    play sound retreat loop

    narrator "身后传来屏障破碎的巨响与骑士的怒吼，马库斯联合镇上隐藏的守护者，暂时拖住了追兵。一路疾驰，你们彻底远离了霜鸦镇。"
    pause 2.0

    scene bg forest_road with fade:
        vp
    play bgm bgm_solemn fadeout 1.0 fadein 2.0
    stop retreat

    narrator "林间雨声渐小，夜色慢慢褪去，天边泛起拂晓微光。你体内的刺痛逐渐消退，可身体依旧酸软乏力。"
    show char karen_normal at left
    show char isold_normal at right:
        zoom(1.4)

    isold "全力爆发血脉力量的反噬很严重吧？这股火焰太过霸道，往后千万不要在未掌握力量前强行催动。"
    karen "我明白。直到现在，我依旧不清楚这股力量的来历，也不懂他们为何执意追捕我。"

    isold "(望向东方幽深的密林)"
    isold "羊皮纸上的据点是我们眼下唯一的方向。赶路途中，我们慢慢摸索力量的用法。前路凶险，但二人同行，便无所畏惧。"

    narrator "二人并肩停下脚步，稍作休整。前方的林间长路一望无际，围绕着血脉、力量与阴谋的全新旅程，正式拉开序幕。"
    narrator "【第一章：初次觉醒 · 结伴上路 · 章节结束】"
    jump chapter2_main_line