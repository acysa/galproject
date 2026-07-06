# ==================== 第五章 · 终章【圣庭烬灭·万物归寂】 ====================
# 零变量适配！承接第四章所有分支，无例外全部汇入终末死局
# 所有分歧、离队、被俘、援军、隔阂全部剧情自然收拢，全员全灭唯一结局

label end_all:
    scene bg town_outside_night with dissolve:
        vp
    play bgm bgm_night_tension fadeout 1.0 fadein 2.0

    # 【万能统一承接剧情，适配第四章所有分支，无需任何变量】
    narrator "无论此前路途是并肩同行、隔阂冷战、中途离散、孤身独行，亦或是携族人援军奔赴此地。"
    narrator "王城大教堂早已被大主教的全域黯蚀结界彻底封锁，整片区域时空锁死——所有牵扯献祭阴谋之人，无论身在何处，尽数被黑雾强制牵引至地底献祭核心。"

    # 统一归位所有角色：自然圆上所有第四章分支状态
    narrator "短暂失散的二人在此被迫重聚，先前被俘、离队、独自前行的伊索尔德被结界黑雾牵引至此；驰援而来的隐士与烬火遗民尽数被困法阵领域；溃败的骑士残部、幕后叛徒、始作俑者大主教，无一例外，全员汇聚终焉之地。"

    show char isold_normal at left
    show char karen_normal at right
    show char old_man at center
    show char black_knight_cap at right

    narrator "黑雾翻涌，地下巨型献祭深渊彻底展露全貌，这是大主教早已设下的终末死局。他从一开始就从未打算让任何人活着离开这片献祭领域。"
    play sound altar_hum loop

    old_man "(神色绝望，望着沸腾黑雾)"
    old_man "全域结界……我们所有人，从踏入王城范围的一刻起，就已经是死人了。"

    narrator "叛徒从黑雾中走出，放弃一切挣扎，颓然道出真相。大主教早已将自身魂魄与大陆黯蚀本源绑定，献祭仪式并非为了征服，而是一场**同归于尽的全域湮灭仪式**。"

    narrator "黑刃骑士队长率领最后残军封锁所有退路，决战无可避免，所有人只能联手奋力击碎献祭核心。"
    play sound boss_clash loop
    show effect ember_combine at center with flashbulb
    pause 2.2

    narrator "烬火血脉、遗民之力、隐士传承、双人羁绊尽数迸发，全力击溃骑士残部与叛徒，最终直面畸变大主教。几番死战，法阵核心轰然碎裂。"

    stop boss_clash
    stop altar_hum
    play bgm bgm_sad_break fadein 0.5 fadein 1.5
    play sound crash loop

    # 终末崩塌，全员覆灭（自然收束所有角色）
    narrator "核心崩碎瞬间，被束缚的黯蚀本源彻底暴走，地底岩层瞬间连锁崩塌，无尽腐蚀黑雾喷涌吞噬整座地下圣殿。"
    narrator "大主教随本源炸裂湮灭，临死引爆所有积蓄黯蚀能量，彻底封死所有逃生出口。"

    narrator "坚硬岩层层层坠落，结界锁死空间无人可脱身。隐士为护住族人耗尽灵力葬身废墟，残存烬火遗民尽数被黑雾吞噬。"
    narrator "黑刃骑士军团全员掩埋崩塌之下，持续的腐蚀瘴气撕碎一切战力。"

    narrator "你与伊索尔德的烬火屏障转瞬破碎，一路所有羁绊、仇恨、救赎、抗争，最终尽数淹没在末日崩塌的漆黑深渊之中。"

    # ========== 唯一终结局：全员归寂，故事彻底终结 ==========
label five_end_all_dead_ending:
    scene bg cathedral_abyss_core with dissolve
    stop music
    stop sound
    stop voice

    narrator "大教堂彻底塌陷，整片献祭深渊被千米岩层永久掩埋。"
    narrator "大主教、叛徒、黯蚀骑士全军覆没。"
    narrator "隐士、烬火遗民族群彻底消亡。"
    narrator "大陆最后两支纯血烬火继承者，双双陨落。"

    narrator "百年献祭阴谋终以**所有相关者全员覆灭**落下帷幕。"
    narrator "黑雾散尽，祸乱终结，但世间再无烬火、再无抗争、再无爱恨羁绊。"
    narrator "一切归零，万物归寂。"
    narrator "【终章 · 唯一真结局：圣庭烬灭，全员归寂｜全篇故事彻底完结】"
    return

# ==================== 第五章 单人烬火终线（仅男主独活结局） ====================
# 适配：第四章所有女主离场/被俘/单人独行分支
# 零变量、纯剧情自然承接、独立label不冲突任何旧章节

label end_one:
    scene bg village_sunset with dissolve
    play bgm bgm_hermit_warm fadeout 1.0 fadein 2.0

    narrator "大教堂崩塌、全域黯蚀黑雾消散的数年之后。"
    narrator "那场终末浩劫里，所有人尽数落幕——伊索尔德被俘失踪、隐士覆灭、遗民散尽、骑士与大主教埋骨深渊。整片大陆，只剩你最后一名烬火血脉独自存活。"
    narrator "你放弃了所有复仇与执念，隐去姓名，远离王城与枯林，在偏远小村定居，刻意封存血脉力量，像普通人一样活着。"

    scene bg village_night with dissolve
    play bgm bgm_sad_break fadeout 1.0 fadein 1.5

    narrator "你以为浩劫落幕，余生可以平庸终老。"
    narrator "可教会残存的余孽从未消亡，他们穷尽数年追踪世间最后一缕烬火气息，终究找到了这座偏僻村落。"

    scene bg village_battle with dissolve
    play sound march_armor loop
    play bgm bgm_boss_fight fadeout 1.0

    narrator "深夜黑雾再临，为数不多的残存黯蚀骑士包围小屋。他们不再需要献祭仪式，唯一使命——抹杀大陆最后一名纯血烬火，彻底斩断灾祸根源。"

    show char karen_normal at center
    narrator "数年隐世，你的血脉力量早已生疏、不复巅峰。没有羁绊共鸣、没有战友支援、没有援军相伴。你孤身一人，面对整片教会最后的杀戮军团。"

    play sound boss_clash loop
    show effect ember_combine at center with flashbulb
    pause 2.0

    narrator "你强行解封封存已久的烬火之力，孤身迎战。金色焰光再度亮起，却是整片血脉最后的回光返照。你斩杀无数残敌，却终究寡不敌众，浑身伤痕累累，力量彻底透支枯竭。"

    stop boss_clash
    stop march_armor

    scene bg village_battle with dissolve
    play bgm bgm_sad_break fadeout 0.5 fadein 2.0

    narrator "最后一缕烬火熄灭。"
    narrator "你以凡人之躯抗争至最后一刻，最终倒在满地残戈与夜色之中。"

# 单人专属终结局
label five_end_single_dead:
    scene bg black_empty with dissolve
    stop music
    stop sound
    stop voice

    narrator "世间再无烬火血脉。"
    narrator "那场横跨百年的献祭纷争，没有胜者，没有救赎，没有幸存者。"
    narrator "全员覆灭、独苗凋零、爱恨归零、宿命终末。"
    narrator "【终章 · 隐藏真结局：孤火寂灭，血脉终绝｜全篇彻底完结】"
    return