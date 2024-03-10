import random
quotes = [
    "Romans 15:13- May the God of hope fill you with all joy and peace as you trust in him, so that you may overflow with hope by the power of the Holy Spirit.",
    "Ephesians 3:20 - Now to him who is able to do immeasurably more than all we ask or imagine, according to his power that is at work within us.",
    "Proverbs 3:5-6 - Trust in the Lord with all your heart, and do not lean on your own understanding. In all your ways acknowledge him, and he will make straight your paths.",
    "Proverbs 31:28 - Her children rise up and call her blessed; Her husband also, and he praises her.",
    "Psalm 107:1 - Give thanks to the Lord, for He is good; his love endures forever.",
    "Philippians 4:13 - I can do all things through Christ who strengthens me.",
    "Isaiah 40:31 - But those who hope in the Lord will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint.",
    "Psalm 23:1 - The Lord is my shepherd; I shall not want.",
    "Matthew 6:33 - But seek first his kingdom and his righteousness, and all these things will be given to you as well.",  
    "John 3:16 - For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.",
    "Jeremiah 29:11 - For I know the plans I have for you,” declares the Lord, “plans to prosper you and not to harm you, plans to give you hope and a future.",
    "1 Corinthians 16:14 - Do everything in love."
    "Psalm 46:1 - God is our refuge and strength, an ever-present help in trouble.",
    "Romans 8:28 - And we know that in all things God works for the good of those who love him, who have been called according to his purpose.",
    "Galatians 5:22-23 - But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control. Against such things there is no law.",
    "James 1:17 - Every good and perfect gift is from above, coming down from the Father of the heavenly lights, who does not change like shifting shadows.",
    "2 Timothy 1:7 - For God has not given us a spirit of fear, but of power and of love and of a sound mind.",
    "Matthew 11:28-30 - Come to me, all you who are weary and burdened, and I will give you rest. Take my yoke upon you and learn from me, for I am gentle and humble in heart, and you will find rest for your souls. For my yoke is easy and my burden is light.",
    "Psalm 37:4 - Delight yourself in the Lord, and he will give you the desires of your heart.",
    "1 Peter 5:7 - Cast all your anxiety on him because he cares for you.",
    "Romans 12:2 - Do not conform to the pattern of this world, but be transformed by the renewing of your mind. Then you will be able to test and approve what Gods will is—his good, pleasing and perfect will.",
    "Psalm 119:105 - Your word is a lamp for my feet, a light on my path.",
    "Proverbs 16:3 - Commit to the Lord whatever you do, and he will establish your plans.",
    "Isaiah 41:10 - So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand.",
    "John 14:6 - Jesus answered, 'I am the way and the truth and the life. No one comes to the Father except through me.",
    "Psalm 46:10 - He says, 'Be still, and know that I am God; I will be exalted among the nations, I will be exalted in the earth.",
    "1 John 4:18 - There is no fear in love. But perfect love drives out fear, because fear has to do with punishment. The one who fears is not made perfect in love.",
    "Colossians 3:23-24 - Whatever you do, work at it with all your heart, as working for the Lord, not for human masters, since you know that you will receive an inheritance from the Lord as a reward. It is the Lord Christ you are serving.",
    "Romans 8:38-39 - For I am convinced that neither death nor life, neither angels nor demons, neither the present nor the future, nor any powers, neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.",
    "Psalm 34:8 - Taste and see that the Lord is good; blessed is the one who takes refuge in him.",
    "Proverbs 17:17 - A friend loves at all times, and a brother is born for a time of adversity.",
    "Matthew 5:16 - In the same way, let your light shine before others, that they may see your good deeds and glorify your Father in heaven.",
    "1 Corinthians 13:13 - And now these three remain: faith, hope and love. But the greatest of these is love.",
    "Psalm 37:4 - Delight yourself in the Lord, and he will give you the desires of your heart.",
    "Proverbs 3:5-6 - Trust in the Lord with all your heart, and do not lean on your own understanding. In all your ways acknowledge him, and he will make straight your paths.",
    "Isaiah 40:31 - But those who hope in the Lord will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint.",
    "Jeremiah 29:11 - For I know the plans I have for you,” declares the Lord, “plans to prosper you and not to harm you, plans to give you hope and a future.",
    "Psalm 23:1 - The Lord is my shepherd; I shall not want.",
    "Matthew 6:33 - But seek first his kingdom and his righteousness, and all these things will be given to you as well.",
    "Romans 12:2 - Do not conform to the pattern of this world, but be transformed by the renewing of your mind. Then you will be able to test and approve what Gods will is—his good, pleasing and perfect will.",
    "Philippians 4:6-7 - Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.",
    "Psalm 27:1 - The Lord is my light and my salvation—whom shall I fear? The Lord is the stronghold of my life—of whom shall I be afraid?",
    "Proverbs 3:5 - Trust in the Lord with all your heart and lean not on your own understanding.",
    "Isaiah 43:2 - When you pass through the waters, I will be with you; and when you pass through the rivers, they will not sweep over you. When you walk through the fire, you will not be burned; the flames will not set you ablaze.",
    "John 14:27 - Peace I leave with you; my peace I give you. I do not give to you as the world gives. Do not let your hearts be troubled and do not be afraid.",
    "Romans 8:31 - What, then, shall we say in response to these things? If God is for us, who can be against us?",
    "Ephesians 2:8-9 - For it is by grace you have been saved, through faith—and this is not from yourselves, it is the gift of God—not by works, so that no one can boast.",
    "Philippians 4:19 - And my God will meet all your needs according to the riches of his glory in Christ Jesus.",
    "1 Thessalonians 5:16-18 - Rejoice always, pray continually, give thanks in all circumstances; for this is God’s will for you in Christ Jesus.",
    "Hebrews 13:8 - Jesus Christ is the same yesterday and today and forever.",
    "James 1:2-4 - Consider it pure joy, my brothers and sisters, whenever you face trials of many kinds, because you know that the testing of your faith produces perseverance. Let perseverance finish its work so that you may be mature and complete, not lacking anything.",
    "1 Peter 5:7 - Cast all your anxiety on him because he cares for you.",
    "1 John 1:9 - If we confess our sins, he is faithful and just and will forgive us our sins and purify us from all unrighteousness.",
    "Genesis 1:1 - In the beginning God created the heavens and the earth.",
    "Psalm 37:7 - Be still before the Lord and wait patiently for him; do not fret when people succeed in their ways, when they carry out their wicked schemes.",
    "Isaiah 26:3 - You will keep in perfect peace those whose minds are steadfast because they trust in you.",
    "Matthew 11:28 - Come to me, all you who are weary and burdened, and I will give you rest.",
    "Luke 1:37 - For no word from God will ever fail.",
    "John 10:10 - The thief comes only to steal and kill and destroy; I have come that they may have life, and have it to the full.",
    "Acts 16:31 - They replied, 'Believe in the Lord Jesus, and you will be saved—you and your household.'",
    "Romans 5:8 - But God demonstrates his own love for us in this: While we were still sinners, Christ died for us.",
    "1 Corinthians 10:13 - No temptation has overtaken you except what is common to mankind. And God is faithful; he will not let you be tempted beyond what you can bear. But when you are tempted, he will also provide a way out so that you can endure it.",
    "Galatians 5:22-23 - But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness, and self-control. Against such things there is no law.",
    "Ephesians 4:32 - Be kind and compassionate to one another, forgiving each other, just as in Christ God forgave you.",
    "Philippians 4:13 - I can do all this through him who gives me strength.",
    "Colossians 3:17 - And whatever you do, whether in word or deed, do it all in the name of the Lord Jesus, giving thanks to God the Father through him.",
]

# displaying first qoute
ran_quote = random.choice(quotes)
print ("\033[1m" + ran_quote + "\033[0m")


while True:
    answer = input("Do you want to see another qoute? (Yes/No): ").lower()
    if answer == "yes" or answer == "y":
        ran_quote = random.choice(quotes)
        print ("\033[1m" + ran_quote + "\033[0m")
        continue
    else:
        break
