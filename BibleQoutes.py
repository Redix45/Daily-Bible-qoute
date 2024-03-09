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
