"""目錄
10---冰淇淋蛋糕
140--冰棒
290--長條
0----0
0----0
0----0
"""
products = {
    "mango-cake": {
        "id": "mango-cake",
        "name": "芒果冰淇淋蛋糕",
        "image": "https://hackmd.io/_uploads/ryUVFiQ4eg.jpg",
        "short": "季節限定芒果冰淇淋蛋糕，嚴選愛文芒果製作，果香濃郁，清爽滑順超消暑。",
        "detail": "嚴選當季愛文芒果製作，果肉香甜多汁，與濃郁奶香冰淇淋完美融合。綿密蛋糕體搭配滑順口感，層層堆疊出酸甜清爽的夏日風味，是不可錯過的芒果季限定甜點！",
        "category": "ice_cream_cake",
        "unit": "吋",
        "sizes": {
            "4": 480,
            "6": 980,
            "8": 1480
        }
    },
    "vanilla-chocolate-cake": {
        "id": "vanilla-chocolate-cake",
        "name": "香草巧克力冰淇淋蛋糕",
        "image": "https://lh6.googleusercontent.com/PpNP3MtQr3bDhgEBBVWBt6x9gH-6X7x49EQ87n_ZcuVkQm-pjKzkAjVTy6wyh_k20cgXj28-rLkORnvNSMdZN7y2PB_vIYMEk1NLGBU7R0o11MmtOeuZiwbj_9F6PvtnpkHd7nex99HsASgTNK-9J8kj99cmQJiSZR_nv7LBQyxCjMMJhQ=w260?key=f3LMdrebQNMgqn96gxJSfw",
        "short": "香草的柔滑遇上濃郁巧克力，層層交融，甜而不膩，入口即化的經典冰淇淋蛋糕。",
        "detail": "香草牛奶冰淇淋的細緻奶香，搭配法芙娜巧克力的濃郁可可香，層層堆疊出香濃又滑順的口感。蛋糕底層加入巧酥脆片，增添咬感，是一款大人小孩都會愛上的經典冰淇淋蛋糕。",
        "category": "ice_cream_cake",
        "unit": "吋",
        "sizes": {
            "4": 480,
            "6": 980,
            "8": 1480
        }
    },
    "berries-cake": {
        "id": "berries-cake",
        "name": "綜合莓果冰淇淋蛋糕",
        "image": "https://lh4.googleusercontent.com/-Sa_GCkb3RH317i07sQxtxez-dt0Jn6YABuaiP-OD7og3zZoSglAaY6fcN1tF0jsi9zlLELCZ9NHoAsIMCOpTv2RGJ0-aMRPMXYBIgw0Bsqqu4QquQDYdX4w2Oa3O8JTc7aDKulhY-mN7RqMDjdfBQsvgmealJTZyiOzaYK1tP9iZ0yvbw=w260?key=f3LMdrebQNMgqn96gxJSfw",
        "short": "綜合莓果酸甜濃郁，搭配香濃冰淇淋與繽紛水果，層層口感，清爽又幸福。",
        "detail": "綜合莓果酸甜濃郁，搭配香濃冰淇淋與繽紛水果，層層口感，清爽又幸福。",
        "category": "ice_cream_cake",
        "unit": "吋",
        "sizes": {
            "4": 480,
            "6": 980,
            "8": 1480
        }
    },
    "pearl-milk-tea-cake": {
        "id": "pearl-milk-tea-cake",
        "name": "珍珠奶茶冰淇淋蛋糕",
        "image": "https://hackmd.io/_uploads/rylaxj1egg.jpg",
        "short": "經典珍珠奶茶變身冰淇淋蛋糕，Q彈珍珠搭配濃郁奶茶，冰涼又療癒！",
        "detail": "現熬茶香融合奶香滑順，搭配Q彈珍珠，還原最熟悉的珍珠奶茶冰淇淋蛋糕。",
        "category": "ice_cream_cake",
        "unit": "吋",
        "sizes": {
            "4": 480,
            "6": 980,
            "8": 1480
        }
    },
    "milk-strawberry-cake": {
        "id": "milk-strawberry-cake",
        "name": "草莓牛奶冰淇淋蛋糕",
        "image": "https://hackmd.io/_uploads/HJnt1r7eex.jpg",
        "short": "冰涼微甜的天然草莓🍓，幸福美味首選。",
        "detail": "草莓牛奶香甜融合，搭配繽紛水果與冰淇淋球，綿密滑順，入口滿是幸福滋味。",
        "category": "ice_cream_cake",
        "unit": "吋",
        "sizes": {
            "4": 480,
            "6": 980,
            "8": 1480
        }
    },
    "milk-peanut-cake": {
        "id": "milk-peanut-cake",
        "name": "花生牛奶冰淇淋蛋糕",
        "image": "https://lh5.googleusercontent.com/fEypdajlNOr_VHB-PA5nHUxbk--7tUSJT4wagCbmWQaoKGAen6BCjTthSh77Uo9ciAQKJ-dQV2EpdqQFIqNGdYGDf7tQotFC8JrXx9q5vqUcTSQ15hsCtOxLkvMOIv7CKKKwiPWUnEs8lRWcHGEMwDXQXvP3HnRoPdiizrNmZdyqXqLkgA=w260?key=f3LMdrebQNMgqn96gxJSfw",
        "short": "濃郁花生醬融合奶香，綿密香滑、香氣十足。",
        "detail": "嚴選香醇花生醬與鮮奶調和製作，口感濃郁滑順，入口帶有花生顆粒的香氣與咬感。搭配酥脆餅乾底，是一款經典又耐吃的冰淇淋蛋糕，深受大人小孩喜愛。",
        "category": "ice_cream_cake",
        "unit": "吋",
        "sizes": {
            "4": 480,
            "6": 980,
            "8": 1480
        }
    },
    "chocolate-strawberry-cake": {
        "id": "chocolate-strawberry-cake",
        "name": "草莓巧克力冰淇淋蛋糕",
        "image": "https://lh4.googleusercontent.com/jpxOLDKsRmTNT9x5cK6MnfQk9Px4zlU588_MtjQu7BmE33oBVrlWOyFBJMOcDD0_biwWSwhPLnqH1WY10tyfmJ8AfqgPMF6yx7T3caXa7WpKkEuZ2asY4GG-Vs91lTNqVy8oFftNfrZJ7qoXcMjNdWlZYqjjyooMi_PN14qykb6RGlMLCA=w260?key=f3LMdrebQNMgqn96gxJSfw",
        "short": "香甜草莓遇上濃醇巧克力，酸甜層次口感超迷人。",
        "detail": "使用新鮮草莓製成冰淇淋，酸甜清香，搭配法芙娜巧克力冰淇淋的濃郁苦甜，兩種風味交織出完美層次。底層酥脆餅乾增添口感，是一款視覺與味覺兼具的夢幻冰淇淋蛋糕。",
        "category": "ice_cream_cake",
        "unit": "吋",
        "sizes": {
            "4": 480,
            "6": 980,
            "8": 1480
        }
    },
    "matcha-cake": {
        "id": "matcha-cake",
        "name": "小山園抹茶拿鐵冰淇淋蛋糕",
        "image": "https://hackmd.io/_uploads/SyHmFikeeg.png",
        "short": "小山園抹茶＋紅豆內餡，苦甜層次豐富。",
        "detail": "採用日本宇治抹茶，搭配自家熬煮紅豆餡，成熟大人氣的推薦選擇。",
        "category": "ice_cream_cake",
        "unit": "吋",
        "sizes": {
            "4": 480,
            "6": 980,
            "8": 1480
        }
    },
    "platter-cake": {
        "id": "platter-cake",
        "name": "冰淇淋蛋糕拼盤",
        "image": "https://lh3.googleusercontent.com/OokxLPG_a9Tp3zli3iew9HEUqe6b1g_DaXCrpfmP0m39RdiW6XWIgPdd_SJxCMXh9n_pSxGsoJqSxoNBy5S3rkUYtRLXP_6N2zogi0IL3TRObyvq30uNvFMIEO0NH-eHWjDurg3HzLMPhlWNM2rardphmK1Kp3cTieLyM0KC1ph8gug7OQ=w260?key=f3LMdrebQNMgqn96gxJSfw",
        "short": "多種口味一次滿足，冰淇淋蛋糕拼盤超級療癒。",
        "detail": "精選多款人氣口味冰淇淋蛋糕組成拼盤。色彩繽紛、口感豐富，適合聚會分享或送禮，是冰友最愛的高人氣甜點選擇。",
        "category": "ice_cream_cake",
        "unit": "吋",
        "sizes": {
            "4": 480,
            "6": 980,
            "8": 1480
        }
    },

####################################################################################
    
    "vanilla-popsicle": {
        "id": "vanilla-popsicle",
        "name": "香草牛奶冰棒",
        "image": "https://lh7-rt.googleusercontent.com/formsz/AN7BsVBRWGNTvPaCujeg8iyW3zmBx4IdhRpKlSR-t-j5biM2e8pdTd4KeYhDS5spD6fLyuT_XO3q-aHdtSKmseGbz4Mcx3NAGQjfnYv3tEMos7kP9CQ3-IgP7EbDNJxXfzNnDk80RwPyfW0xlKugbEQeqBv8=w260?key=W1w9LWLVB2PoIVnkMhJERA",
        "short": "使用真實香草精製作，奶香濃郁滑順，經典香草冰棒，簡單卻讓人回味無窮。",
        "detail": "嚴選香草莢萃取天然香草精，搭配濃醇鮮奶製作，無添加香料與色素。口感滑順、甜而不膩，是老少咸宜的經典口味，純粹自然，每一口都吃得安心又滿足。",
        "category": "popsicle",
        "unit": "支",
        "sizes": {
            "1": 35,
        }
    },
    "peanut-popsicle": {
        "id": "peanut-popsicle",
        "name": "花生冰棒",
        "image": "https://lh7-rt.googleusercontent.com/formsz/AN7BsVBEwsh6E59isASC-GTKI9ZuiG85OrPaTLkxlKKL_qZ-SzYk8V1OJfe-6OWMAA7oidY0o9ElZA2nWsw46PSmWVunBPmTYpjf297B8a9bnagAT3fMgTIqWbK9clOok61P-e-lrdgxGoFubUa_eqMePs7M=w260?key=W1w9LWLVB2PoIVnkMhJERA",
        "short": "濃郁花生醬融合鮮奶製作，香氣十足，口感滑順，傳統又不失驚喜。",
        "detail": "選用香氣濃厚的花生醬，結合鮮奶調和出滑順質地。每一口都能品嚐到花生的真實風味，是懷舊系冰棒中的經典代表。",
        "category": "popsicle",
        "unit": "支",
        "sizes": {
            "1": 35,
        }
    },
    "oreo-milk-popsicle": {
        "id": "oreo-milk-popsicle",
        "name": "OREO牛奶冰棒",
        "image": "https://lh7-rt.googleusercontent.com/formsz/AN7BsVDfuqmWrE_Oy2OAMwA5bnHd0m2N67yfAY_DJ9MRBYLUUmb3fClwo-GprOttDZJGApNyjXGa1hwfxPMytpflkbzKR6yHfFZ9VImcrkEsVhy0SeZmTy4zw9Jop830b9pieidMO1XD8JXoj1GUCIC23-VWAA=w260?key=W1w9LWLVB2PoIVnkMhJERA",
        "short": "香濃鮮奶中加入OREO碎片，口感豐富酥脆，是大人小孩都愛的甜點系冰棒。",
        "detail": "以滑順牛奶冰淇淋為基底，拌入大量OREO餅乾碎片，甜中帶脆，每一口都像在吃餅乾＋冰淇淋，讓人愛不釋手。",
        "category": "popsicle",
        "unit": "支",
        "sizes": {
            "1": 45,
        }
    },
    ###
    ###
    ###
    "chocolate-popsicle": {
        "id": "chocolate-popsicle",
        "name": "巧克力冰棒",
        "image": "https://drive.google.com/u/0/drive-viewer/AKGpihYXTSuipvMmIAb3PZAvS4R6tLxalnfWL-gbglNnMl8wbleDIbvcuMaoslrkVgn8cHgJD__biDbuajZLQP-RCcjV1bEUA8A_LJw=s1600-rw-v1",
        "short": "使用法芙娜可可粉製作，濃郁香醇，苦甜平衡，是真正巧克力控的最愛。",
        "detail": "嚴選高品質可可粉製作，香氣濃郁、口感滑順，甜中帶苦、層次分明。不加香料的純粹巧克力風味，是大人味冰品的代表。",
        "category": "popsicle",
        "unit": "支",
        "sizes": {
            "1": 45,
        }
    },
    "pearl-milk-tea-popsicle": {
        "id": "pearl-milk-tea-popsicle",
        "name": "珍珠奶茶冰棒",
        "image": "https://drive.google.com/u/0/drive-viewer/AKGpihYXTSuipvMmIAb3PZAvS4R6tLxalnfWL-gbglNnMl8wbleDIbvcuMaoslrkVgn8cHgJD__biDbuajZLQP-RCcjV1bEUA8A_LJw=s1600-rw-v1",
        "short": "採用現熬茶湯製成奶茶冰體，搭配Q彈珍珠，還原經典珍奶口感。",
        "detail": "不使用茶粉，而是用上等茶葉現煮熬製，融合奶香冰體，入口茶韻回甘。搭配手工珍珠，咬感十足，還原最熟悉的台式風味。",
        "category": "popsicle",
        "unit": "支",
        "sizes": {
            "1": 45,
        }
    },
    "macadamia-nuts-popsicle": {
        "id": "macadamia-nuts-popsicle",
        "name": "夏威夷果仁冰棒",
        "image": "https://drive.google.com/u/0/drive-viewer/AKGpihYXTSuipvMmIAb3PZAvS4R6tLxalnfWL-gbglNnMl8wbleDIbvcuMaoslrkVgn8cHgJD__biDbuajZLQP-RCcjV1bEUA8A_LJw=s1600-rw-v1",
        "short": "濃醇奶香冰體中加入夏威夷果仁，香脆滑順，口感層次豐富。",
        "detail": "奶香濃郁的冰體搭配香脆夏威夷果仁，每一口都能吃到堅果碎粒，綿密與酥脆交融，是愛吃堅果者的冰品首選。",
        "category": "popsicle",
        "unit": "支",
        "sizes": {
            "1": 45,
        }
    },
    "strawberry-popsicle": {
        "id": "strawberry-popsicle",
        "name": "草莓冰棒",
        "image": "https://lh7-rt.googleusercontent.com/formsz/AN7BsVDpmHVN9KulT4JsW8VS3MoGqhAqKWX09I2j0WcpgP-R1c7a_mz7tUdv7qSrIZwmLxVkHn3mvP_oZTCI0Df6cAiyOpeRhj1cSUnCFDHqWKeg0Kcyqa5F6DvRgUbSjj9emmBtUzbHFVP7nEIjeshocWME=w260?key=W1w9LWLVB2PoIVnkMhJERA",
        "short": "嚴選新鮮草莓打製，果香濃郁，酸甜適中，彷彿戀愛的滋味。",
        "detail": "使用台灣草莓製成果泥，保留天然果香與微酸口感。冰體滑順、甜度適中，是炎炎夏日中最能喚醒味蕾的夢幻口味。",
        "category": "popsicle",
        "unit": "支",
        "sizes": {
            "1": 45,
        }
    },
    "berries-popsicle": {
        "id": "berries-popsicle",
        "name": "綜合莓果冰棒",
        "image": "https://lh7-rt.googleusercontent.com/formsz/AN7BsVC4w2KzjHBoidwQUAijbSPELQjMjrDTDf5e8NggUSGbrw3fELtbwglsh6kLFlxp9n4jN6R77dZDjSQVOOTFSVYpMvJlFuqAb-M4EAvzLfVA8NP-E3-upZFsNtGNT__JRDJxi7bP59Xq85HI87WWXYxn=w260?key=W1w9LWLVB2PoIVnkMhJERA",
        "short": "多種莓果混合製作，果香層次豐富，酸甜平衡，充滿夏日清爽感。",
        "detail": "融合藍莓、覆盆子、小紅莓等多種莓果，口感層層堆疊、果香十足。每一口都充滿果肉纖維與酸甜風味，是莓果控的最愛。",
        "category": "popsicle",
        "unit": "支",
        "sizes": {
            "1": 45,
        }
    },
    "matcha-popsicle": {
        "id": "matcha-popsicle",
        "name": "抹茶冰棒",
        "image": "https://lh7-rt.googleusercontent.com/formsz/AN7BsVAM2v4BBEFr_w6fIbdcUEVHB0dwtknX8c_2oUr0FYTiNy5-s7C5qZav-_-N_G2MSAZ-I2X4t_qaagHkvgUy1TXpUsDNhtbHkv2tORZM3bBLrrVDklMTFiiWYjPhlggaI5-iJlAod_b8mKVR-5ow0l6x=w260?key=W1w9LWLVB2PoIVnkMhJERA",
        "short": "使用日本小山園抹茶，茶香濃郁微苦，回甘清爽，是抹茶控必吃的冰棒。",
        "detail": "嚴選日本小山園抹茶粉製作，不加香料與色素，保留抹茶原始的清香與微苦回甘。口感滑順不甜膩，尾韻淡雅，是大人味冰棒的代表，適合喜愛日式風味的你。",
        "category": "popsicle",
        "unit": "支",
        "sizes": {
            "1": 45,
        }
    },
    "red-beans-popsicle": {
        "id": "red-beans-popsicle",
        "name": "紅豆冰棒",
        "image": "https://lh7-rt.googleusercontent.com/formsz/AN7BsVBhURUDaHBk69exUYLpn_i9yi6dNM2Gli2DqsvDuE7QaE8RzpGvI-EN25Tn9s3Sh2vJHyxDQ-mpM5FWyDU4xglT4_PkHYK7qxxaskVK_PSDfg7OnLxIvx0Zf6AQNN-llfdO6zuLulW51DzLDv8RNt8ExQ=w260?key=W1w9LWLVB2PoIVnkMhJERA",
        "short": "嚴選台灣紅豆熬煮，保留顆粒口感，甜而不膩，懷舊經典風味。",
        "detail": "使用台灣紅豆慢火熬煮，紅豆顆顆飽滿，保留天然香氣與口感。冰體綿密、紅豆香濃，是從小吃到大的懷舊冰棒，甜度剛好、吃得到家的味道。",
        "category": "popsicle",
        "unit": "支",
        "sizes": {
            "1": 45,
        }
    },
    "blueberry-popsicle": {
        "id": "blueberry-popsicle",
        "name": "藍莓冰棒",
        "image": "https://lh7-rt.googleusercontent.com/formsz/AN7BsVDuEZIPxdTj6De8K2M2Fuiz_9zwzeVQksd1ksX2HWjz2JtnFyq9-_ppe8n7N1AY54msKPISLlSzQ0YS36Fn6Ij_ziVXeyehWe771II9Uo8Ez2ztjmFvqUzK-XJRsmGjieh3__hz1ExE8256h1l_C1R4uw=w260?key=W1w9LWLVB2PoIVnkMhJERA",
        "short": "使用藍莓果肉打製，果香濃郁微酸，顏色天然、清爽解膩。",
        "detail": "以新鮮藍莓製成果泥冰體，保留藍莓自然酸甜與深紫色澤，不添加色素香料。每一口都能感受到果粒香氣與微酸清爽，是喜歡果香系的冰友首選。",
        "category": "popsicle",
        "unit": "支",
        "sizes": {
            "1": 45,
        }
    },
    "coffee-popsicle": {
        "id": "coffee-popsicle",
        "name": "咖啡冰棒",
        "image": "https://lh7-rt.googleusercontent.com/formsz/AN7BsVAaVwFyUpspAOV46XWhx29BKq3EGAhtuBk5IRorJ1NZuP0vA-sjg3b44SVkslSzVahnmcjLTDqZ0SuoRnsJK0YyOmaJo51vBkI9MAzPzlIHj2Z4k-oYimZx2ASdiLxfQh893UlT7rrPqP3ykWOiFluODA=w260?key=W1w9LWLVB2PoIVnkMhJERA",
        "short": "使用藍莓果肉打製，果香濃郁微酸，顏色天然、清爽解膩。",
        "detail": "以新鮮藍莓製成果泥冰體，保留藍莓自然酸甜與深紫色澤，不添加色素香料。每一口都能感受到果粒香氣與微酸清爽，是喜歡果香系的冰友首選。",
        "category": "popsicle",
        "unit": "支",
        "sizes": {
            "1": 45,
        }
    },

####################################################################################
"""
    "pearl-milk-tea-long": {
        "id": "pearl-milk-tea-long",
        "name": "珍珠奶茶長條蛋糕",
        "image": "https://lh7-rt.googleusercontent.com/formsz/AN7BsVA79CVL1JRWoineC3dof2t4s1C23srcj98SiehTRrzrnSW3Hp6dQLItCv59ZgcVpPt_54FpweqauKmujfUuFi5Y5a9-d5Qvm9AAcUmLwb2-EiO3d6VYQ9RFnvmv9RuJFa3789YwVPoASYklas7r2GU6XQ=w260?key=W1w9LWLVB2PoIVnkMhJERA",
        "short": "經典珍珠奶茶變身冰淇淋蛋糕，Q彈珍珠搭配濃郁奶茶，冰涼又療癒！",
        "detail": "現熬茶香融合奶香滑順，搭配Q彈珍珠，還原最熟悉的珍珠奶茶冰淇淋蛋糕。",
        "category": "long-cake",
        "unit": "支",
        "sizes": {
            "1": 480,
        }
    },
    """
}
activities = [
    
]


