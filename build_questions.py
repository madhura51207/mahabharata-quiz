# build_questions.py - Generates the rich Mahabharata Question Bank
import json

questions = [
    # =========================================================================
    # KIDS (Ages 6–10)
    # =========================================================================
    # Characters
    {
        "id": "k_char_1",
        "ageGroup": "kids",
        "category": "characters",
        "difficulty": "easy",
        "question": "Who was the legendary archer among the five Pandava brothers?",
        "options": ["Arjuna", "Bhima", "Nakula", "Sahadeva"],
        "answer": 0,
        "explanation": "Arjuna was the third Pandava brother and celebrated as the finest archer of his age."
    },
    {
        "id": "k_char_2",
        "ageGroup": "kids",
        "category": "characters",
        "difficulty": "easy",
        "question": "Which Pandava brother was famous for his colossal strength and love for sweets and delicious food?",
        "options": ["Bhima", "Sahadeva", "Yudhishthira", "Nakula"],
        "answer": 0,
        "explanation": "Bhima had the strength of thousands of elephants and loved hearty feasts!"
    },
    {
        "id": "k_char_3",
        "ageGroup": "kids",
        "category": "characters",
        "difficulty": "easy",
        "question": "Who was Arjuna's beloved friend and charioteer during the great war?",
        "options": ["Lord Krishna", "Balarama", "Guru Drona", "King Shalya"],
        "answer": 0,
        "explanation": "Lord Krishna guided Arjuna's chariot as Parthasarathy and gave the immortal wisdom of the Gita."
    },
    {
        "id": "k_char_4",
        "ageGroup": "kids",
        "category": "characters",
        "difficulty": "medium",
        "question": "Who was the eldest brother among the hundred Kaurava princes?",
        "options": ["Dushasana", "Duryodhana", "Vikarna", "Yuyutsu"],
        "answer": 1,
        "explanation": "Duryodhana was the eldest son of King Dhritarashtra and Queen Gandhari."
    },
    {
        "id": "k_char_5",
        "ageGroup": "kids",
        "category": "characters",
        "difficulty": "medium",
        "question": "Which young tribal prince learned archery by practicing before a clay statue of Guru Drona?",
        "options": ["Abhimanyu", "Ekalavya", "Ghatotkacha", "Upamanyu"],
        "answer": 1,
        "explanation": "Ekalavya practiced tirelessly before a clay statue of Dronacharya and became a master archer."
    },
    {
        "id": "k_char_6",
        "ageGroup": "kids",
        "category": "characters",
        "difficulty": "hard",
        "question": "Which elephant-headed deity wrote down the Mahabharata as Sage Vyasa recited it?",
        "options": ["Lord Ganesha", "Lord Kartikeya", "Lord Indra", "Sage Narada"],
        "answer": 0,
        "explanation": "Lord Ganesha agreed to act as scribe on the condition that Sage Vyasa spoke continuously without pause."
    },
    {
        "id": "k_char_7",
        "ageGroup": "kids",
        "category": "characters",
        "difficulty": "medium",
        "question": "Who was the loyal magical son of Bhima and Hidimbi who fought bravely in the night?",
        "options": ["Ghatotkacha", "Abhimanyu", "Iravan", "Parikshit"],
        "answer": 0,
        "explanation": "Ghatotkacha possessed magical powers and was a tremendous ally to the Pandavas."
    },
    {
        "id": "k_char_8",
        "ageGroup": "kids",
        "category": "characters",
        "difficulty": "easy",
        "question": "Which teacher taught martial arts and archery to both Pandavas and Kauravas when they were young?",
        "options": ["Guru Dronacharya", "Guru Vasishtha", "Guru Vishwamitra", "Sage Valmiki"],
        "answer": 0,
        "explanation": "Guru Dronacharya was the royal preceptor appointed by Grandfather Bhishma to train the princes."
    },

    # Stories & Events (Kids)
    {
        "id": "k_stories_1",
        "ageGroup": "kids",
        "category": "stories",
        "difficulty": "easy",
        "question": "During the archery test on the tree, what part of the toy bird did Arjuna see?",
        "options": ["Only the eye of the bird", "The entire bird and branches", "The sky and clouds", "The golden tree trunk"],
        "answer": 0,
        "explanation": "Arjuna told Guru Drona: 'I see only the eye of the bird.' This single-pointed focus made him supreme."
    },
    {
        "id": "k_stories_2",
        "ageGroup": "kids",
        "category": "stories",
        "difficulty": "easy",
        "question": "How many Pandava brothers were there in total?",
        "options": ["Five", "Three", "Seven", "Ten"],
        "answer": 0,
        "explanation": "The five brothers were Yudhishthira, Bhima, Arjuna, Nakula, and Sahadeva."
    },
    {
        "id": "k_stories_3",
        "ageGroup": "kids",
        "category": "stories",
        "difficulty": "medium",
        "question": "What flammable material was the trick palace of Lakshagriha built from?",
        "options": ["Lac (meltable wax)", "Stone and marble", "Iron beams", "Solid gold"],
        "answer": 0,
        "explanation": "Duryodhana had Lakshagriha made of lac and resin, but the Pandavas escaped through a secret tunnel."
    },
    {
        "id": "k_stories_4",
        "ageGroup": "kids",
        "category": "stories",
        "difficulty": "hard",
        "question": "At Draupadi's swayamvara, how did Arjuna aim his arrow at the spinning fish target?",
        "options": ["By looking down at its reflection in water", "By closing his eyes", "From behind a royal curtain", "By riding a moving chariot"],
        "answer": 0,
        "explanation": "Arjuna looked down into a pool of water/oil and pierced the eye of the revolving target overhead."
    },
    {
        "id": "k_stories_5",
        "ageGroup": "kids",
        "category": "stories",
        "difficulty": "medium",
        "question": "What magic vessel did the Sun god gift to the Pandavas to feed anyone as long as Draupadi had not eaten?",
        "options": ["Akshaya Patra", "Kamadhenu Pot", "Amrita Kalasha", "Sudarshana Bowl"],
        "answer": 0,
        "explanation": "The Akshaya Patra provided unending food each day until Queen Draupadi finished her meal."
    },
    {
        "id": "k_stories_6",
        "ageGroup": "kids",
        "category": "stories",
        "difficulty": "easy",
        "question": "Which game did Shakuni invite Yudhishthira to play that led to their forest exile?",
        "options": ["Game of Dice", "Hide and Seek", "Horse Racing", "Tug of War"],
        "answer": 0,
        "explanation": "Shakuni lured Yudhishthira into an unfair game of dice, causing the Pandavas to lose their kingdom."
    },

    # Weapons & Astras (Kids)
    {
        "id": "k_weapons_1",
        "ageGroup": "kids",
        "category": "weapons",
        "difficulty": "easy",
        "question": "What is the famous name of Arjuna's celestial bow?",
        "options": ["Gandiva", "Pinaka", "Sharanga", "Vijaya"],
        "answer": 0,
        "explanation": "Gandiva was gifted to Arjuna by Agni, along with inexhaustible quivers that never ran out of arrows."
    },
    {
        "id": "k_weapons_2",
        "ageGroup": "kids",
        "category": "weapons",
        "difficulty": "medium",
        "question": "What heavy weapon did Bhima master and swing with great power?",
        "options": ["Mace (Gada)", "Dagger", "Crossbow", "Net"],
        "answer": 0,
        "explanation": "Bhima was known as the supreme mace-warrior (Gada-dhari) of his era."
    },
    {
        "id": "k_weapons_3",
        "ageGroup": "kids",
        "category": "weapons",
        "difficulty": "hard",
        "question": "What golden protective armor and earrings was hero Karna born wearing?",
        "options": ["Kavacha and Kundala", "Vajra Crown", "Chandra Crest", "Surya Belt"],
        "answer": 0,
        "explanation": "Karna was born with natural golden armor (Kavacha) and earrings (Kundala) from his father Surya."
    },
    {
        "id": "k_weapons_4",
        "ageGroup": "kids",
        "category": "weapons",
        "difficulty": "easy",
        "question": "Which spinning discus weapon belongs to Lord Krishna?",
        "options": ["Sudarshana Chakra", "Trishula", "Brahmastra", "Vajra"],
        "answer": 0,
        "explanation": "Lord Krishna commands the spinning, radiant Sudarshana Chakra on his index finger."
    },

    # Places (Kids)
    {
        "id": "k_places_1",
        "ageGroup": "kids",
        "category": "places",
        "difficulty": "easy",
        "question": "Where was the 18-day great battle of the Mahabharata fought?",
        "options": ["Kurukshetra", "Ayodhya", "Lanka", "Kishkindha"],
        "answer": 0,
        "explanation": "The battle occurred at Kurukshetra, known as the field of Dharma (Dharmakshetra)."
    },
    {
        "id": "k_places_2",
        "ageGroup": "kids",
        "category": "places",
        "difficulty": "medium",
        "question": "What was the capital city of the Kuru Kingdom where the palace stood?",
        "options": ["Hastinapura", "Indraprastha", "Mathura", "Varanasi"],
        "answer": 0,
        "explanation": "Hastinapura, situated near the holy Ganga, was the royal capital of the Kuru rulers."
    },
    {
        "id": "k_places_3",
        "ageGroup": "kids",
        "category": "places",
        "difficulty": "hard",
        "question": "What magnificent city did the Pandavas create with palaces that dazzled like magic?",
        "options": ["Indraprastha", "Dwaraka", "Panchala", "Ujjain"],
        "answer": 0,
        "explanation": "Indraprastha was built so wondrously that pools looked like polished floors and floors looked like water."
    },
    {
        "id": "k_places_4",
        "ageGroup": "kids",
        "category": "places",
        "difficulty": "easy",
        "question": "Which golden island city by the western sea was ruled by Lord Krishna?",
        "options": ["Dwaraka", "Rameshwaram", "Kashi", "Haridwar"],
        "answer": 0,
        "explanation": "Lord Krishna ruled Dwaraka, an architectural wonder surrounded by the shimmering Arabian Sea."
    },

    # Relationships (Kids)
    {
        "id": "k_rel_1",
        "ageGroup": "kids",
        "category": "relationships",
        "difficulty": "easy",
        "question": "Who was the mother of Yudhishthira, Bhima, and Arjuna?",
        "options": ["Queen Kunti", "Queen Gandhari", "Queen Madri", "Queen Satyavati"],
        "answer": 0,
        "explanation": "Queen Kunti was mother to the three elder Pandavas and raised all five brothers with immense love."
    },
    {
        "id": "k_rel_2",
        "ageGroup": "kids",
        "category": "relationships",
        "difficulty": "medium",
        "question": "Who was the mother of the twin brothers Nakula and Sahadeva?",
        "options": ["Queen Madri", "Queen Kunti", "Queen Gandhari", "Queen Rukmini"],
        "answer": 0,
        "explanation": "Queen Madri was King Pandu's second wife and the mother of Nakula and Sahadeva."
    },
    {
        "id": "k_rel_3",
        "ageGroup": "kids",
        "category": "relationships",
        "difficulty": "hard",
        "question": "Who was the elder brother of Lord Krishna who always carried a plow?",
        "options": ["Balarama", "Vasudeva", "Pradyumna", "Aniruddha"],
        "answer": 0,
        "explanation": "Balarama was Krishna's strong, protective elder brother and a master of mace fighting."
    },
    {
        "id": "k_rel_4",
        "ageGroup": "kids",
        "category": "relationships",
        "difficulty": "easy",
        "question": "What was the relationship between the Pandavas and the hundred Kauravas?",
        "options": ["They were first cousins", "They were father and sons", "They were uncle and nephews", "They were strangers"],
        "answer": 0,
        "explanation": "King Pandu and King Dhritarashtra were brothers, making their sons first cousins."
    },

    # Values & Lessons (Kids)
    {
        "id": "k_val_1",
        "ageGroup": "kids",
        "category": "values",
        "difficulty": "easy",
        "question": "Which virtue was the eldest Pandava, Yudhishthira, most famous for upholding?",
        "options": ["Truth and Honesty", "Anger", "Pride", "Greed"],
        "answer": 0,
        "explanation": "Yudhishthira was revered as 'Dharmaraja' because he consistently chose truth and fairness."
    },
    {
        "id": "k_val_2",
        "ageGroup": "kids",
        "category": "values",
        "difficulty": "medium",
        "question": "What does Arjuna's test with the bird's eye teach all of us in school and life?",
        "options": ["Laser focus on your goal brings success", "Look around at distractions", "Give up when tasks are hard", "Rely on luck alone"],
        "answer": 0,
        "explanation": "True excellence comes from ignoring distractions and keeping full attention on the objective."
    },
    {
        "id": "k_val_3",
        "ageGroup": "kids",
        "category": "values",
        "difficulty": "hard",
        "question": "Why is Karna called 'Dana Veera' (Hero of Charity)?",
        "options": ["He never turned away anyone who asked for help", "He won every race", "He had the largest army", "He lived in the tallest palace"],
        "answer": 0,
        "explanation": "Karna's generosity was boundless; he gave away gold, jewels, and even his divine armor to those in need."
    },
    {
        "id": "k_val_4",
        "ageGroup": "kids",
        "category": "values",
        "difficulty": "easy",
        "question": "What does the friendship between Lord Krishna and poor Sudama show us?",
        "options": ["True friendship looks at love and kindness, not wealth", "Only rich people can be friends", "Presents must be very expensive", "Kings never talk to childhood friends"],
        "answer": 0,
        "explanation": "Krishna embraced Sudama with tears of joy, demonstrating that genuine friendship transcends wealth."
    },

    # =========================================================================
    # YOUNG LEARNERS (Ages 11–15)
    # =========================================================================
    # Characters
    {
        "id": "yl_char_1",
        "ageGroup": "young_learners",
        "category": "characters",
        "difficulty": "easy",
        "question": "Who took the stern vow of lifelong celibacy ('Bhishma Pratigya') to make his father Shantanu happy?",
        "options": ["Devavrata (Bhishma)", "Vichitravirya", "Chitrangada", "Kripa"],
        "answer": 0,
        "explanation": "Devavrata's selfless vow earned him the name Bhishma ('the formidable') and the boon of Ichha Mrityu."
    },
    {
        "id": "yl_char_2",
        "ageGroup": "young_learners",
        "category": "characters",
        "difficulty": "medium",
        "question": "Which sixteen-year-old warrior son of Arjuna heroically breached the Chakravyuha formation?",
        "options": ["Abhimanyu", "Iravan", "Babruvahana", "Parikshit"],
        "answer": 0,
        "explanation": "Abhimanyu learned how to enter the circular Chakravyuha while in his mother Subhadra's womb."
    },
    {
        "id": "yl_char_3",
        "ageGroup": "young_learners",
        "category": "characters",
        "difficulty": "hard",
        "question": "Who was appointed supreme commander of the Pandava forces for the Kurukshetra battle?",
        "options": ["Dhrishtadyumna", "Satyaki", "Arjuna", "Drupada"],
        "answer": 0,
        "explanation": "Dhrishtadyumna, born from the sacred sacrificial fire of King Drupada, led the seven Pandava divisions."
    },
    {
        "id": "yl_char_4",
        "ageGroup": "young_learners",
        "category": "characters",
        "difficulty": "medium",
        "question": "Which mighty king of Magadha was born in two halves and later wrestled with Bhima?",
        "options": ["Jarasandha", "Shishupala", "Kamsa", "Dantavakra"],
        "answer": 0,
        "explanation": "Jarasandha was joined together by the demoness Jara; Bhima ultimately split him in two to defeat him."
    },
    {
        "id": "yl_char_5",
        "ageGroup": "young_learners",
        "category": "characters",
        "difficulty": "hard",
        "question": "Who was the royal priest and preceptor of the Pandavas during their forest travels?",
        "options": ["Dhaumya", "Kashyapa", "Parashara", "Markandeya"],
        "answer": 0,
        "explanation": "Sage Dhaumya guided the Pandavas with spiritual rites, hymns, and counsel throughout their exile."
    },

    # Stories & Events (Young Learners)
    {
        "id": "yl_stories_1",
        "ageGroup": "young_learners",
        "category": "stories",
        "difficulty": "easy",
        "question": "How long was the total exile imposed upon the Pandavas after the second dice match?",
        "options": ["12 years in forest + 1 year in disguise", "14 years in forest only", "10 years in forest + 3 years in town", "18 years across realms"],
        "answer": 0,
        "explanation": "They spent 12 years in the forest followed by 1 year of Agyatvasa (incognito), where discovery meant another 12 years exile."
    },
    {
        "id": "yl_stories_2",
        "ageGroup": "young_learners",
        "category": "stories",
        "difficulty": "medium",
        "question": "In the kingdom of Virata during their year in hiding, what role did Bhima assume in the royal kitchens?",
        "options": ["Ballava the master cook", "Kanka the dice master", "Granthika the horse trainer", "Tantipala the cowherd"],
        "answer": 0,
        "explanation": "Bhima went by the name Ballava, delighting the king with exceptional culinary arts and wrestling."
    },
    {
        "id": "yl_stories_3",
        "ageGroup": "young_learners",
        "category": "stories",
        "difficulty": "hard",
        "question": "What disguise did Arjuna adopt while living in King Virata's palace?",
        "options": ["Brihannala, teacher of dance and music", "Ballava, wrestler", "Kanka, court advisor", "Vaideha, merchant"],
        "answer": 0,
        "explanation": "Due to Urvashi's temporary curse, Arjuna lived as Brihannala, teaching music and fine arts to Princess Uttara."
    },
    {
        "id": "yl_stories_4",
        "ageGroup": "young_learners",
        "category": "stories",
        "difficulty": "medium",
        "question": "How many days did the epic battle of Kurukshetra last?",
        "options": ["18 days", "12 days", "21 days", "24 days"],
        "answer": 0,
        "explanation": "The war lasted exactly 18 days, with the Mahabharata divided into 18 Parvas (books)."
    },

    # Weapons & Astras (Young Learners)
    {
        "id": "yl_weapons_1",
        "ageGroup": "young_learners",
        "category": "weapons",
        "difficulty": "easy",
        "question": "From which supreme deity did Arjuna obtain the invincible Pashupatastra after rigorous penance?",
        "options": ["Lord Shiva", "Lord Indra", "Lord Brahma", "Lord Varuna"],
        "answer": 0,
        "explanation": "Lord Shiva, appearing disguised as a hunter (Kirata), tested Arjuna's valor before bestowing the Pashupatastra."
    },
    {
        "id": "yl_weapons_2",
        "ageGroup": "young_learners",
        "category": "weapons",
        "difficulty": "medium",
        "question": "Which deadly weapon did Indra give to Karna in exchange for his celestial Kavacha and Kundala?",
        "options": ["Vasavi Shakti", "Brahmastra", "Narayanastra", "Varunastra"],
        "answer": 0,
        "explanation": "Indra granted the Vasavi Shakti, which possessed the power to guarantee one kill before returning to heaven."
    },
    {
        "id": "yl_weapons_3",
        "ageGroup": "young_learners",
        "category": "weapons",
        "difficulty": "hard",
        "question": "Which supreme weapon of Lord Vishnu was unleashed by Ashwatthama, countered only by total surrender?",
        "options": ["Narayanastra", "Brahmashira", "Agneyastra", "Vayuastra"],
        "answer": 0,
        "explanation": "The Narayanastra intensified against fighting resistance; laying down arms and submitting neutralized it completely."
    },
    {
        "id": "yl_weapons_4",
        "ageGroup": "young_learners",
        "category": "weapons",
        "difficulty": "medium",
        "question": "What is the name of Lord Krishna's sacred conch shell whose roar terrified the enemy ranks?",
        "options": ["Panchajanya", "Devadatta", "Poundra", "Anantavijaya"],
        "answer": 0,
        "explanation": "Lord Krishna blew Panchajanya, which he obtained after defeating the demon Panchajana."
    },

    # Places (Young Learners)
    {
        "id": "yl_places_1",
        "ageGroup": "young_learners",
        "category": "places",
        "difficulty": "easy",
        "question": "In which city did Draupadi's father King Drupada rule his prosperous kingdom?",
        "options": ["Panchala (Kampilya)", "Hastinapura", "Magadha", "Chedi"],
        "answer": 0,
        "explanation": "Kampilya was the capital of the southern Panchala realm ruled by King Drupada."
    },
    {
        "id": "yl_places_2",
        "ageGroup": "young_learners",
        "category": "places",
        "difficulty": "medium",
        "question": "What was the name of the kingdom where the Pandavas spent their 13th year incognito?",
        "options": ["Matsya Kingdom", "Kashi", "Anga", "Gandhara"],
        "answer": 0,
        "explanation": "King Virata ruled the Matsya Kingdom, where all five brothers and Draupadi lived without being uncovered."
    },
    {
        "id": "yl_places_3",
        "ageGroup": "young_learners",
        "category": "places",
        "difficulty": "hard",
        "question": "In which forest did the Pandavas spend the largest portion of their 12-year forest exile?",
        "options": ["Kamyaka and Dwaita forests", "Dandakaranya", "Ashokavana", "Panchavati"],
        "answer": 0,
        "explanation": "The Pandavas dwelled predominantly in the Kamyaka and Dwaita forests on the banks of Saraswati."
    },

    # Relationships (Young Learners)
    {
        "id": "yl_rel_1",
        "ageGroup": "young_learners",
        "category": "relationships",
        "difficulty": "easy",
        "question": "What was the family relationship between Lord Krishna and Queen Kunti?",
        "options": ["Kunti was Krishna's paternal aunt (father's sister)", "They were cousins", "Kunti was Krishna's mother", "They had no relation"],
        "answer": 0,
        "explanation": "Kunti (born Pritha) was the sister of Vasudeva, making her Krishna's paternal aunt (Bua)."
    },
    {
        "id": "yl_rel_2",
        "ageGroup": "young_learners",
        "category": "relationships",
        "difficulty": "medium",
        "question": "Who was the mother of Abhimanyu and the sister of Krishna and Balarama?",
        "options": ["Subhadra", "Rukmini", "Draupadi", "Ulupi"],
        "answer": 0,
        "explanation": "Subhadra was married to Arjuna and gave birth to their heroic son Abhimanyu."
    },
    {
        "id": "yl_rel_3",
        "ageGroup": "young_learners",
        "category": "relationships",
        "difficulty": "hard",
        "question": "Who was the demoness sister of Hidimba who married Bhima in the deep forest?",
        "options": ["Hidimbi", "Surpanakha", "Simhika", "Tataka"],
        "answer": 0,
        "explanation": "Hidimbi admired Bhima's noble character and married him with Kunti's blessings."
    },

    # Values & Lessons (Young Learners)
    {
        "id": "yl_val_1",
        "ageGroup": "young_learners",
        "category": "values",
        "difficulty": "easy",
        "question": "Why did Arjuna collapse in sorrow at the beginning of the battle of Kurukshetra?",
        "options": ["He was heartbroken at the thought of fighting his beloved teachers and kin", "He had forgotten his weapons", "He was afraid of the enemy numbers", "He did not like chariot riding"],
        "answer": 0,
        "explanation": "Seeing Grandfather Bhishma and Guru Drona, Arjuna was overcome with grief, leading to Krishna's sermon of the Gita."
    },
    {
        "id": "yl_val_2",
        "ageGroup": "young_learners",
        "category": "values",
        "difficulty": "medium",
        "question": "What does the renowned verse 'Karmanye Vadhikaraste Ma Phaleshu Kadachana' teach?",
        "options": ["Do your rightful duty without anxious obsession over the reward", "Never work hard", "Always demand victory first", "Leave everything to fate without doing work"],
        "answer": 0,
        "explanation": "You have a right to perform your prescribed duty, but never to the fruits of your actions."
    },
    {
        "id": "yl_val_3",
        "ageGroup": "young_learners",
        "category": "values",
        "difficulty": "hard",
        "question": "Why did Yudhishthira refuse to step into Indra's celestial chariot without the faithful dog at Mount Meru?",
        "options": ["He believed abandoning a loyal soul who sought refuge was against Dharma", "The dog had wings", "He wanted to hunt in paradise", "The chariot was too small"],
        "answer": 0,
        "explanation": "Dharma in the form of a dog tested Yudhishthira's steadfast compassion and loyalty toward the vulnerable."
    },

    # =========================================================================
    # STUDENTS (Ages 16–20)
    # =========================================================================
    # Characters
    {
        "id": "st_char_1",
        "ageGroup": "students",
        "category": "characters",
        "difficulty": "easy",
        "question": "Who received divine vision (Divya Drishti) from Sage Vyasa to provide a live account of the war to King Dhritarashtra?",
        "options": ["Sanjaya", "Vidura", "Kripa", "Dhaumya"],
        "answer": 0,
        "explanation": "Sanjaya could witness every incident, thought, and word on the battlefield and relayed it to the blind monarch."
    },
    {
        "id": "st_char_2",
        "ageGroup": "students",
        "category": "characters",
        "difficulty": "medium",
        "question": "Which Kaurava brother boldly condemned Draupadi's disrobing in the royal assembly hall?",
        "options": ["Vikarna", "Yuyutsu", "Chitrasena", "Dussaha"],
        "answer": 0,
        "explanation": "Vikarna courageously stood up against his elders and brothers, arguing that Draupadi was gambled unlawfully."
    },
    {
        "id": "st_char_3",
        "ageGroup": "students",
        "category": "characters",
        "difficulty": "hard",
        "question": "Which warrior was Princess Amba reborn as to avenge her dishonor against Bhishma?",
        "options": ["Shikhandi", "Dhrishtadyumna", "Uttamaujas", "Satyajit"],
        "answer": 0,
        "explanation": "Reborn as King Drupada's child Shikhandi, Bhishma refused to strike someone who had been born a woman."
    },
    {
        "id": "st_char_4",
        "ageGroup": "students",
        "category": "characters",
        "difficulty": "medium",
        "question": "Who killed Guru Dronacharya after Drona laid down his weapons in grief?",
        "options": ["Dhrishtadyumna", "Bhima", "Arjuna", "Satyaki"],
        "answer": 0,
        "explanation": "Dhrishtadyumna, born from sacrificial fire destined to slay Drona, beheaded the meditating master."
    },
    {
        "id": "st_char_5",
        "ageGroup": "students",
        "category": "characters",
        "difficulty": "hard",
        "question": "Which son of Dhritarashtra crossed over to the Pandava army on the first day of war to fight for Dharma?",
        "options": ["Yuyutsu", "Vikarna", "Durmukha", "Somadatta"],
        "answer": 0,
        "explanation": "When Yudhishthira proclaimed an open invitation before combat, Yuyutsu alone chose the side of righteousness."
    },

    # Stories & Events (Students)
    {
        "id": "st_stories_1",
        "ageGroup": "students",
        "category": "stories",
        "difficulty": "easy",
        "question": "In the Yaksha Prashna, who turned out to be the mysterious Yaksha questioning Yudhishthira?",
        "options": ["Yama (Lord Dharma)", "Lord Indra", "Lord Brahma", "Sage Brihaspati"],
        "answer": 0,
        "explanation": "Lord Dharma tested his spiritual son Yudhishthira's wisdom, righteousness, and impartiality."
    },
    {
        "id": "st_stories_2",
        "ageGroup": "students",
        "category": "stories",
        "difficulty": "medium",
        "question": "Before the war, when Arjuna and Duryodhana sought Krishna's help, what did Arjuna choose?",
        "options": ["An unarmed Krishna alone as guide", "Krishna's million-strong Narayani army", "The royal palace of Dwaraka", "Krishna's divine weapons"],
        "answer": 0,
        "explanation": "Arjuna prioritized Krishna's divine presence and moral guidance over immense physical military power."
    },
    {
        "id": "st_stories_3",
        "ageGroup": "students",
        "category": "stories",
        "difficulty": "hard",
        "question": "How did Lord Krishna help Arjuna fulfill his vow to slay Jayadratha before sunset on the 14th day?",
        "options": ["By concealing the sun temporarily with the Sudarshana Chakra", "By invoking Varuna's rainstorm", "By reversing the rotation of the earth", "By stopping time"],
        "answer": 0,
        "explanation": "Krishna created the illusion of sunset; Jayadratha revealed himself in celebration, and Arjuna struck."
    },
    {
        "id": "st_stories_4",
        "ageGroup": "students",
        "category": "stories",
        "difficulty": "medium",
        "question": "How did Guru Drona come to believe that his beloved son Ashwatthama had died in battle?",
        "options": ["Bhima killed an elephant named Ashwatthama, and Yudhishthira confirmed the name", "A messenger brought a false royal scroll", "Sanjaya told him in a vision", "Ashwatthama dropped his bow and fled"],
        "answer": 0,
        "explanation": "Yudhishthira stated 'Ashwatthama is dead,' muttering 'the elephant' under his breath, shaking Drona's resolve."
    },

    # Weapons & Astras (Students)
    {
        "id": "st_weapons_1",
        "ageGroup": "students",
        "category": "weapons",
        "difficulty": "easy",
        "question": "Which supreme weapon was directed by Ashwatthama against the womb of Uttara?",
        "options": ["Brahmashira Astra", "Pashupatastra", "Vaishnavastra", "Varunastra"],
        "answer": 0,
        "explanation": "Ashwatthama unleashed the Brahmashira to extinguish the Pandava dynasty; Krishna entered the womb to protect Parikshit."
    },
    {
        "id": "st_weapons_2",
        "ageGroup": "students",
        "category": "weapons",
        "difficulty": "medium",
        "question": "What is the name of Arjuna's conch shell blown at the start of battle?",
        "options": ["Devadatta", "Poundra", "Anantavijaya", "Panchajanya"],
        "answer": 0,
        "explanation": "Arjuna blew Devadatta ('gift of the gods'), gifted to him by King Maya / Lord Indra."
    },
    {
        "id": "st_weapons_3",
        "ageGroup": "students",
        "category": "weapons",
        "difficulty": "hard",
        "question": "Which divine bow was given to Karna by his guru, Bhagavan Parashurama?",
        "options": ["Vijaya", "Kodanda", "Gandiva", "Pinaka"],
        "answer": 0,
        "explanation": "The Vijaya bow, crafted by Vishwakarma, guaranteed invulnerability to its wielder while strung."
    },
    {
        "id": "st_weapons_4",
        "ageGroup": "students",
        "category": "weapons",
        "difficulty": "medium",
        "question": "How did Arjuna counter the terrifying fiery Agneyastra fired by the Kauravas?",
        "options": ["By releasing the Varunastra (water weapon)", "By raising a bronze shield", "By hiding behind Krishna", "By firing a stone bolt"],
        "answer": 0,
        "explanation": "Varunastra, the weapon of water deity Varuna, created torrents of rain to extinguish the blazing firestorm."
    },

    # Places (Students)
    {
        "id": "st_places_1",
        "ageGroup": "students",
        "category": "places",
        "difficulty": "easy",
        "question": "In which sacred forest did Ugrasrava Sauti narrate the entire Mahabharata to gathered sages?",
        "options": ["Naimisharanya", "Dandakaranya", "Panchavati", "Khandavaprastha"],
        "answer": 0,
        "explanation": "Sage Shaunaka and fellow rishis hosted the grand twelve-year sacrifice in Naimisharanya forest."
    },
    {
        "id": "st_places_2",
        "ageGroup": "students",
        "category": "places",
        "difficulty": "medium",
        "question": "Which kingdom did Shalya rule before Duryodhana tricked him with luxurious royal hospitality?",
        "options": ["Madra Kingdom", "Gandhara", "Sindhu", "Anga"],
        "answer": 0,
        "explanation": "Shalya, uncle to Nakula and Sahadeva, ruled Madra and felt obligated by honor to fight for Duryodhana."
    },
    {
        "id": "st_places_3",
        "ageGroup": "students",
        "category": "places",
        "difficulty": "hard",
        "question": "Where did the Pandavas hide their celestial weapons during their year in disguise?",
        "options": ["Inside a hollow Shami tree near a burial ground", "At the bottom of Lake Dwaipayana", "Inside a mountain cavern", "Beneath the palace throne"],
        "answer": 0,
        "explanation": "They wrapped the weapons in a corpse-cloth and tied them up in a massive Shami tree outside Virata."
    },

    # Relationships (Students)
    {
        "id": "st_rel_1",
        "ageGroup": "students",
        "category": "relationships",
        "difficulty": "easy",
        "question": "Who was Vidura considered an earthly incarnation of?",
        "options": ["Lord Dharma (Yama)", "Sage Brihaspati", "Vayu", "Lord Varuna"],
        "answer": 0,
        "explanation": "Due to Sage Mandavya's curse, Lord Dharma was incarnated as Vidura, the voice of pure ethical statecraft."
    },
    {
        "id": "st_rel_2",
        "ageGroup": "students",
        "category": "relationships",
        "difficulty": "medium",
        "question": "Which Naga princess married Arjuna during his twelve-year pilgrimage and revived him in later life?",
        "options": ["Ulupi", "Chitrangada", "Kadru", "Vinata"],
        "answer": 0,
        "explanation": "Ulupi, daughter of the Naga king Kauravya, loved Arjuna and used the Sanjeevani gem to restore his life."
    },
    {
        "id": "st_rel_3",
        "ageGroup": "students",
        "category": "relationships",
        "difficulty": "hard",
        "question": "Who was the father of Guru Dronacharya, born miraculously from a wooden vessel?",
        "options": ["Sage Bharadwaja", "Sage Atri", "Sage Gautama", "Sage Jamadagni"],
        "answer": 0,
        "explanation": "Drona was the son of Maharishi Bharadwaja, one of the revered Saptarishis."
    },

    # Values & Lessons (Students)
    {
        "id": "st_val_1",
        "ageGroup": "students",
        "category": "values",
        "difficulty": "easy",
        "question": "In the Bhagavad Gita, what are the three gateways to ruin mentioned in Chapter 16?",
        "options": ["Lust (Kama), Anger (Krodha), and Greed (Lobha)", "Hunger, Thirst, and Fatigue", "Pride, Ignorance, and Hesitation", "Poverty, Disease, and Envy"],
        "answer": 0,
        "explanation": "Krishna warns that unbridled passion, wrath, and covetousness blind the intellect and destroy the soul."
    },
    {
        "id": "st_val_2",
        "ageGroup": "students",
        "category": "values",
        "difficulty": "medium",
        "question": "Why did Yudhishthira request the Yaksha to revive Nakula instead of his dearest brother Arjuna or Bhima?",
        "options": ["To ensure that both mothers (Kunti and Madri) had one living son", "Nakula was the wisest warrior", "Nakula had magical potions", "He was disappointed in Bhima"],
        "answer": 0,
        "explanation": "Yudhishthira exemplified Anrishamsya (supreme compassion and equity), honouring both his mothers equally."
    },
    {
        "id": "st_val_3",
        "ageGroup": "students",
        "category": "values",
        "difficulty": "hard",
        "question": "What is the core tragedy in Karna's moral dilemma in the Mahabharata?",
        "options": ["Gratitude and personal loyalty to a flawed friend clashing with universal righteousness (Dharma)", "Lack of archery skill", "A desire to rule the world by force", "Refusing to fight any duel"],
        "answer": 0,
        "explanation": "Karna's tragic narrative highlights the conflict between individual obligation/gratitude and cosmic moral law."
    },

    # =========================================================================
    # ADULTS (Ages 21+)
    # =========================================================================
    # Characters
    {
        "id": "ad_char_1",
        "ageGroup": "adults",
        "category": "characters",
        "difficulty": "easy",
        "question": "Which grandson of Bhima possessed three divine arrows capable of ending the war in moments?",
        "options": ["Barbarika (Khatu Shyam)", "Meghavarna", "Anjanaparvan", "Iravan"],
        "answer": 0,
        "explanation": "Barbarika vowed to fight for the losing side; to prevent universal annihilation, Krishna asked for his head in charity."
    },
    {
        "id": "ad_char_2",
        "ageGroup": "adults",
        "category": "characters",
        "difficulty": "medium",
        "question": "Who was the charioteer of Karna on the decisive 17th day of battle who continually demoralized him?",
        "options": ["King Shalya", "Sanjaya", "Kripacharya", "Ashwatthama"],
        "answer": 0,
        "explanation": "Shalya agreed to steer Karna's chariot at Duryodhana's request, but had secretly promised Yudhishthira to dampen Karna's spirit."
    },
    {
        "id": "ad_char_3",
        "ageGroup": "adults",
        "category": "characters",
        "difficulty": "hard",
        "question": "Who was the sage whose curse on King Parikshit led to the recitation of the Srimad Bhagavatam?",
        "options": ["Shringi", "Samika", "Kavasha", "Durvasa"],
        "answer": 0,
        "explanation": "Enraged that Parikshit draped a lifeless serpent around his father Samika, young Shringi cursed the king to die in seven days."
    },
    {
        "id": "ad_char_4",
        "ageGroup": "adults",
        "category": "characters",
        "difficulty": "medium",
        "question": "Which elder warrior remained on the bed of arrows until the sun entered Uttarayana?",
        "options": ["Bhishma Pitamaha", "Dronacharya", "Bhurisravas", "Balarama"],
        "answer": 0,
        "explanation": "Possessing the boon of Ichha Mrityu, Bhishma chose the auspicious northern solstice (Uttarayana) to leave his body."
    },
    {
        "id": "ad_char_5",
        "ageGroup": "adults",
        "category": "characters",
        "difficulty": "hard",
        "question": "Who was the sage who performed the Putrakameshti yajna for King Drupada resulting in Draupadi and Dhrishtadyumna?",
        "options": ["Yaja and Upayaja", "Vasishta", "Agastya", "Rishyasringa"],
        "answer": 0,
        "explanation": "Sages Yaja and Upayaja conducted the potent fire sacrifice to bestow children capable of defeating Drona."
    },

    # Stories & Events (Adults)
    {
        "id": "ad_stories_1",
        "ageGroup": "adults",
        "category": "stories",
        "difficulty": "easy",
        "question": "In which Parva (book) of the Mahabharata does the Bhagavad Gita appear?",
        "options": ["Bhishma Parva", "Udyoga Parva", "Shanti Parva", "Drona Parva"],
        "answer": 0,
        "explanation": "The Bhagavad Gita comprises chapters 23 through 40 of the Bhishma Parva, the sixth book."
    },
    {
        "id": "ad_stories_2",
        "ageGroup": "adults",
        "category": "stories",
        "difficulty": "medium",
        "question": "In the tragic Sauptika Parva, who led the night-time assault on the sleeping Pandava encampment?",
        "options": ["Ashwatthama", "Kripa", "Kritavarma", "Shakuni"],
        "answer": 0,
        "explanation": "Grief-stricken by Drona's death, Ashwatthama breached warrior codes by slaughtering the sleeping warriors at midnight."
    },
    {
        "id": "ad_stories_3",
        "ageGroup": "adults",
        "category": "stories",
        "difficulty": "hard",
        "question": "What curse did Queen Gandhari cast upon Lord Krishna in the Stri Parva following the war's devastation?",
        "options": ["That the Yadava clan would perish through fratricide within 36 years", "That Dwaraka would fall to foreign invaders", "That Krishna would lose his memories", "That his descendants would never rule"],
        "answer": 0,
        "explanation": "Holding Krishna responsible for failing to avert the slaughter, Gandhari pronounced the 36-year doom upon the Vrishnis."
    },
    {
        "id": "ad_stories_4",
        "ageGroup": "adults",
        "category": "stories",
        "difficulty": "medium",
        "question": "What sacrifice did King Janamejaya conduct to eradicate all snakes after his father Parikshit was bitten by Takshaka?",
        "options": ["Sarpa Satra", "Ashvamedha", "Rajasuya", "Paundarika"],
        "answer": 0,
        "explanation": "The great snake sacrifice (Sarpa Satra) was halted by the young sage Astika before Takshaka was drawn into the pyre."
    },

    # Weapons & Astras (Adults)
    {
        "id": "ad_weapons_1",
        "ageGroup": "adults",
        "category": "weapons",
        "difficulty": "easy",
        "question": "What was the name of the personal bow of Karna crafted by Vishwakarma for Lord Shiva?",
        "options": ["Vijaya", "Gandiva", "Kodanda", "Sharanga"],
        "answer": 0,
        "explanation": "Passed from Shiva to Indra, then Parashurama, the Vijaya bow endowed its bearer with impenetrable defenses."
    },
    {
        "id": "ad_weapons_2",
        "ageGroup": "adults",
        "category": "weapons",
        "difficulty": "medium",
        "question": "Which three curses converged to cause Karna's downfall on the 17th day of battle?",
        "options": ["Parashurama's amnesia curse, a Brahmin's chariot wheel curse, and the Earth goddess curse", "Indra's thunderbolt curse, Agni's burn curse, and Drona's ban", "Surya's shadow curse, Yama's tether, and Shiva's gaze", "Kunti's silence, Draupadi's vow, and Bhima's blow"],
        "answer": 0,
        "explanation": "He forgot the Brahmastra formula at his moment of dire need, while his chariot wheel sank irretrievably into the earth."
    },
    {
        "id": "ad_weapons_3",
        "ageGroup": "adults",
        "category": "weapons",
        "difficulty": "hard",
        "question": "What classification in ancient Indian warfare denoted a hero capable of battling 60,000 warriors at once?",
        "options": ["Maharatha", "Atiratha", "Rathi", "Ardharatha"],
        "answer": 0,
        "explanation": "A Maharatha was capable of vanquishing 60,000 standard combatants simultaneously with mastery of celestial weaponry."
    },
    {
        "id": "ad_weapons_4",
        "ageGroup": "adults",
        "category": "weapons",
        "difficulty": "medium",
        "question": "When King Bhagadatta launched the lethal Vaishnavastra at Arjuna, how did Lord Krishna intervene?",
        "options": ["Krishna stood in front and turned the missile into a fragrant flower garland", "Krishna deflected it with his mace", "Krishna blew it away with his breath", "Arjuna cut it into seven pieces"],
        "answer": 0,
        "explanation": "As the supreme manifestation of Vishnu, Krishna reclaimed his own celestial astra harmlessly around his neck."
    },

    # Places (Adults)
    {
        "id": "ad_places_1",
        "ageGroup": "adults",
        "category": "places",
        "difficulty": "easy",
        "question": "In which lake did Duryodhana hide using water-solidifying magic before the final mace duel with Bhima?",
        "options": ["Dwaipayana Lake", "Bindu Sarovar", "Pampa Sarovar", "Manasarovar"],
        "answer": 0,
        "explanation": "Duryodhana sealed himself beneath the waters of Dwaipayana Sarovar until provoked out by the Pandavas."
    },
    {
        "id": "ad_places_2",
        "ageGroup": "adults",
        "category": "places",
        "difficulty": "medium",
        "question": "At which holy pilgrimage site did Lord Krishna conclude his earthly incarnation after being struck by hunter Jara?",
        "options": ["Bhalka Tirth (Prabhas Patan)", "Mathura Ghats", "Vrindavan Kunj", "Gokul"],
        "answer": 0,
        "explanation": "Bhalka Tirth near Somnath marks the sacred ground where Krishna reclined under a banyan tree."
    },
    {
        "id": "ad_places_3",
        "ageGroup": "adults",
        "category": "places",
        "difficulty": "hard",
        "question": "What is the name of the Himalayan staircase ridge the Pandavas climbed on their final pilgrimage (Mahaprasthanika Parva)?",
        "options": ["Swargarohini", "Nanda Devi", "Trishul Peak", "Kamet"],
        "answer": 0,
        "explanation": "Swargarohini ('pathway to heaven') was the formidable mountain path where each traveler fell save Yudhishthira."
    },

    # Relationships (Adults)
    {
        "id": "ad_rel_1",
        "ageGroup": "adults",
        "category": "relationships",
        "difficulty": "easy",
        "question": "Who fathered Dhritarashtra, Pandu, and Vidura through the ancient tradition of Niyoga?",
        "options": ["Sage Veda Vyasa", "Bhishma", "Sage Parashara", "King Shantanu"],
        "answer": 0,
        "explanation": "At Queen Satyavati's request, Sage Vyasa fathered the royal heirs to preserve the Kuru dynasty."
    },
    {
        "id": "ad_rel_2",
        "ageGroup": "adults",
        "category": "relationships",
        "difficulty": "medium",
        "question": "Who was Kripacharya's twin sister who married Guru Dronacharya?",
        "options": ["Kripi", "Arushi", "Gautami", "Saradwati"],
        "answer": 0,
        "explanation": "Kripi married Dronacharya and became the devoted mother of Ashwatthama."
    },
    {
        "id": "ad_rel_3",
        "ageGroup": "adults",
        "category": "relationships",
        "difficulty": "hard",
        "question": "What were the names of the five sons of Draupadi (Upapandavas)?",
        "options": ["Prativindhya, Sutasoma, Srutakarma, Satanika, and Srutasena", "Abhimanyu, Iravan, Babruvahana, Ghatotkacha, and Parikshit", "Yuyutsu, Vikarna, Durmukha, Chitrasena, and Jalasandha", "Kanka, Ballava, Brihannala, Tantipala, and Granthika"],
        "answer": 0,
        "explanation": "Each Pandava fathered one son with Draupadi: Prativindhya (Yudhishthira), Sutasoma (Bhima), Srutakarma (Arjuna), Satanika (Nakula), and Srutasena (Sahadeva)."
    },

    # Values & Lessons (Adults)
    {
        "id": "ad_val_1",
        "ageGroup": "adults",
        "category": "values",
        "difficulty": "easy",
        "question": "Which Parva contains Bhishma's comprehensive exposition on Rajadharma (statecraft) and Mokshadharma from his bed of arrows?",
        "options": ["Shanti Parva", "Sabha Parva", "Vana Parva", "Udyoga Parva"],
        "answer": 0,
        "explanation": "Shanti Parva is the epic's longest philosophical compendium, teaching governance, justice, and spiritual liberation."
    },
    {
        "id": "ad_val_2",
        "ageGroup": "adults",
        "category": "values",
        "difficulty": "medium",
        "question": "What profound truth does the motto 'Yato Dharmastato Jayah' summarize?",
        "options": ["Where there is righteousness (Dharma), there alone lies true victory", "Victory belongs to whoever strikes first", "Might dictates what is right", "Fate cannot be understood"],
        "answer": 0,
        "explanation": "This celebrated motto emphasizes that ultimate spiritual and lasting triumph aligns with cosmic righteousness."
    },
    {
        "id": "ad_val_3",
        "ageGroup": "adults",
        "category": "values",
        "difficulty": "hard",
        "question": "What is 'Apaddharma', expounded by Bhishma in the Shanti Parva?",
        "options": ["The moral code and actions permissible during times of extreme calamity or crisis", "The duties of ascetics in the forest", "The laws of maritime trade", "Rituals for coronating a king"],
        "answer": 0,
        "explanation": "Apaddharma examines how ethical duties must adapt pragmatically during dire emergency to preserve life and order."
    },

    # --- Additional High-Yield Questions ---
    {
        "id": "k_char_9",
        "ageGroup": "kids",
        "category": "characters",
        "difficulty": "easy",
        "question": "Who was the celestial king of the gods and spiritual father of Arjuna?",
        "options": ["Lord Indra", "Lord Agni", "Lord Vayu", "Lord Surya"],
        "answer": 0,
        "explanation": "Lord Indra was Arjuna's divine father and welcomed him to heaven to train in celestial astras."
    },
    {
        "id": "k_stories_7",
        "ageGroup": "kids",
        "category": "stories",
        "difficulty": "medium",
        "question": "Which sweet cowherd boy grew up in Vrindavan playing his divine flute and eating butter?",
        "options": ["Lord Krishna", "Arjuna", "Dhritarashtra", "Drona"],
        "answer": 0,
        "explanation": "Lord Krishna spent his charming childhood in Gokul and Vrindavan playing his melodious flute."
    },
    {
        "id": "k_weapons_5",
        "ageGroup": "kids",
        "category": "weapons",
        "difficulty": "easy",
        "question": "What unique weapon shaped like a farming tool did Balarama carry into battle?",
        "options": ["Golden Plough (Hala)", "Bow and arrow", "Spear", "Shield"],
        "answer": 0,
        "explanation": "Balarama is fondly called Haladhara because he wielded a golden plough as his trademark weapon."
    },
    {
        "id": "k_places_5",
        "ageGroup": "kids",
        "category": "places",
        "difficulty": "easy",
        "question": "In which village was Lord Krishna raised by Mother Yashoda and Nanda Baba?",
        "options": ["Gokul / Vrindavan", "Ayodhya", "Lanka", "Hastinapura"],
        "answer": 0,
        "explanation": "Krishna was lovingly brought up by Yashoda and Nanda in the pastoral village of Gokul."
    },
    {
        "id": "k_rel_5",
        "ageGroup": "kids",
        "category": "relationships",
        "difficulty": "easy",
        "question": "Who was the foster mother who raised baby Karna with all her love?",
        "options": ["Radha", "Kunti", "Gandhari", "Madri"],
        "answer": 0,
        "explanation": "Radha, wife of charioteer Adhiratha, discovered baby Karna in the basket and raised him with immense love."
    },
    {
        "id": "k_val_5",
        "ageGroup": "kids",
        "category": "values",
        "difficulty": "medium",
        "question": "What does Bhima's protectiveness of his brothers teach us about family?",
        "options": ["Standing up for brothers and sisters with love and courage", "Fighting with siblings over food", "Ignoring family in times of trouble", "Only caring about oneself"],
        "answer": 0,
        "explanation": "Bhima always shielded his mother and younger brothers from every hazard and threat."
    },
    {
        "id": "yl_char_6",
        "ageGroup": "young_learners",
        "category": "characters",
        "difficulty": "medium",
        "question": "Which fierce Yadava hero and student of Arjuna fought tirelessly on the Pandava side?",
        "options": ["Satyaki (Yuyudhana)", "Kritavarma", "Akroora", "Pradyumna"],
        "answer": 0,
        "explanation": "Satyaki was a devoted disciple of Arjuna and one of the finest warriors on the Pandava side."
    },
    {
        "id": "yl_stories_5",
        "ageGroup": "young_learners",
        "category": "stories",
        "difficulty": "medium",
        "question": "Which architect spared by Arjuna during the Khandava fire constructed the magical assembly hall of Indraprastha?",
        "options": ["Maya Danava", "Vishwakarma", "Nala", "Kubera"],
        "answer": 0,
        "explanation": "Grateful for his life, Maya Danava built the famed Maya Sabha filled with optical illusions."
    },
    {
        "id": "yl_weapons_5",
        "ageGroup": "young_learners",
        "category": "weapons",
        "difficulty": "easy",
        "question": "What is the name of Lord Vishnu's celestial bow, often contrasted with Shiva's Pinaka?",
        "options": ["Sharanga", "Gandiva", "Vijaya", "Kodanda"],
        "answer": 0,
        "explanation": "Sharanga is Lord Vishnu's celestial horn-bow, wielded by Krishna during his earthly pastimes."
    },
    {
        "id": "yl_places_4",
        "ageGroup": "young_learners",
        "category": "places",
        "difficulty": "easy",
        "question": "In which city on the banks of Yamuna was Lord Krishna born in King Kamsa's prison?",
        "options": ["Mathura", "Hastinapura", "Dwaraka", "Indraprastha"],
        "answer": 0,
        "explanation": "Krishna appeared at midnight in Mathura to liberate the people from Kamsa's tyrant rule."
    },
    {
        "id": "yl_rel_4",
        "ageGroup": "young_learners",
        "category": "relationships",
        "difficulty": "medium",
        "question": "Who was the renowned martial arts guru who trained Bhishma, Drona, and Karna?",
        "options": ["Bhagavan Parashurama", "Sage Agastya", "Sage Vasishta", "Sage Brihaspati"],
        "answer": 0,
        "explanation": "Parashurama was the warrior sage who instructed Bhishma, Dronacharya, and Karna in advanced warfare."
    },
    {
        "id": "yl_val_4",
        "ageGroup": "young_learners",
        "category": "values",
        "difficulty": "medium",
        "question": "What lesson does Ekalavya's offering of his thumb teach about devotion to a mentor?",
        "options": ["Supreme respect for teachers (Guru Bhakti), though it also raises ethical questions about fairness", "That one should never practice archery", "That teachers must always demand thumbs", "That skill should be kept hidden"],
        "answer": 0,
        "explanation": "Ekalavya's story showcases profound Guru Bhakti while simultaneously highlighting complex ethical challenges in society."
    },
    {
        "id": "st_char_6",
        "ageGroup": "students",
        "category": "characters",
        "difficulty": "easy",
        "question": "Which cousin of Krishna and king of Chedi hurled 100 insults before Krishna ended his life with the Sudarshana Chakra?",
        "options": ["Shishupala", "Dantavakra", "Salva", "Rukmi"],
        "answer": 0,
        "explanation": "Krishna had promised Shishupala's mother to pardon 100 insults; upon the 101st insult at the Rajasuya sacrifice, Krishna struck."
    },
    {
        "id": "st_stories_5",
        "ageGroup": "students",
        "category": "stories",
        "difficulty": "hard",
        "question": "What is the title of the first chapter of the Bhagavad Gita detailing Arjuna's psychological crisis?",
        "options": ["Arjuna Vishada Yoga", "Sankhya Yoga", "Karma Yoga", "Bhakti Yoga"],
        "answer": 0,
        "explanation": "Arjuna Vishada Yoga portrays Arjuna's profound moral crisis, grief, and intellectual breakdown on the battlefield."
    },
    {
        "id": "st_weapons_5",
        "ageGroup": "students",
        "category": "weapons",
        "difficulty": "medium",
        "question": "Which celestial missile harnesses the fury of the wind god to scatter enemy divisions?",
        "options": ["Vayavyastra", "Agneyastra", "Varunastra", "Surya Astra"],
        "answer": 0,
        "explanation": "Vayavyastra invokes the force of Pavana / Vayu, unleashing catastrophic hurricane-force winds."
    },
    {
        "id": "st_places_4",
        "ageGroup": "students",
        "category": "places",
        "difficulty": "medium",
        "question": "Which ancient university city and capital of Gandhara was the homeland of Queen Gandhari and Shakuni?",
        "options": ["Taxila (Takshashila) / Pushkalavati", "Pataliputra", "Avanti", "Kausambi"],
        "answer": 0,
        "explanation": "Gandhara was situated in the north-western frontier, with historical capitals around Pushkalavati and Taxila."
    },
    {
        "id": "st_rel_4",
        "ageGroup": "students",
        "category": "relationships",
        "difficulty": "easy",
        "question": "Who was the biological mother of Karna, who conceived him via the Sun god before marriage?",
        "options": ["Queen Kunti", "Queen Madri", "Queen Gandhari", "Queen Satyavati"],
        "answer": 0,
        "explanation": "Kunti received a mantra from Sage Durvasa; testing it with Lord Surya, she gave birth to Karna."
    },
    {
        "id": "st_val_4",
        "ageGroup": "students",
        "category": "values",
        "difficulty": "medium",
        "question": "What does the concept of 'Nishkama Karma' signify in the Bhagavad Gita?",
        "options": ["Performing one's rightful action selflessly without attachment to fruits or rewards", "Renouncing all work and living in silence", "Working only when high payment is guaranteed", "Performing actions purely for fame"],
        "answer": 0,
        "explanation": "Nishkama Karma is action performed with mental poise, dedication, and freedom from selfish clinging."
    },
    {
        "id": "ad_char_6",
        "ageGroup": "adults",
        "category": "characters",
        "difficulty": "hard",
        "question": "Which aged king of Pragjyotisha fought for the Kauravas riding the fierce elephant Supratika?",
        "options": ["King Bhagadatta", "King Narakasura", "King Shalya", "King Brihadbala"],
        "answer": 0,
        "explanation": "King Bhagadatta was an elderly warrior of formidable prowess who possessed the devastating Vaishnavastra."
    },
    {
        "id": "ad_stories_5",
        "ageGroup": "adults",
        "category": "stories",
        "difficulty": "hard",
        "question": "In which Parva does Sage Markandeya narrate the legendary fidelity story of Savitri and Satyavan to Yudhishthira?",
        "options": ["Vana Parva (Aranyaka Parva)", "Sabha Parva", "Virata Parva", "Udyoga Parva"],
        "answer": 0,
        "explanation": "The story of Savitri confronting Yama to reclaim her husband's soul is recounted in the Vana Parva to comfort Yudhishthira."
    },
    {
        "id": "ad_weapons_5",
        "ageGroup": "adults",
        "category": "weapons",
        "difficulty": "easy",
        "question": "What is the name of King Duryodhana's and Bhima's mace teacher, who remained neutral during the war?",
        "options": ["Lord Balarama", "Guru Drona", "Kripacharya", "Parashurama"],
        "answer": 0,
        "explanation": "Lord Balarama refused to participate in the fratricidal battle and instead departed on a holy pilgrimage."
    },
    {
        "id": "ad_places_4",
        "ageGroup": "adults",
        "category": "places",
        "difficulty": "easy",
        "question": "What is the sacred grove at Kurukshetra where the Bhagavad Gita was traditionally spoken under a banyan tree?",
        "options": ["Jyotisar", "Brahma Sarovar", "Pehowa", "Thanesar"],
        "answer": 0,
        "explanation": "Jyotisar in Kurukshetra is revered as the sanctified ground where Krishna imparted the Gita to Arjuna."
    },
    {
        "id": "ad_rel_4",
        "ageGroup": "adults",
        "category": "relationships",
        "difficulty": "hard",
        "question": "Who was Srutasrava, mother of Shishupala, to whom Krishna gave his vow of 100 pardons?",
        "options": ["Krishna's paternal aunt (Vasudeva's sister)", "Krishna's maternal aunt (Devaki's sister)", "Krishna's grandmother", "Krishna's sister-in-law"],
        "answer": 0,
        "explanation": "Srutasrava was Krishna's paternal aunt (Bua), married to King Damaghosha of Chedi."
    },
    {
        "id": "ad_val_4",
        "ageGroup": "adults",
        "category": "values",
        "difficulty": "hard",
        "question": "What moral dilemma is encapsulated by the term 'Dharma-sankata' in the epic?",
        "options": ["A complex predicament where two valid ethical duties or vows directly conflict", "A violation of legal rules by commoners", "A formal debate between two ascetics", "A curse uttered by a sage"],
        "answer": 0,
        "explanation": "Dharma-sankata denotes the agonizing moral knot where righteous duties oppose one another, demanding deep discernment."
    }
]

print(f"Total curated questions: {len(questions)}")

# Convert to valid JavaScript export
js_content = """/**
 * Mahabharata Quiz - Comprehensive Curated Question Bank
 * Categorized by:
 *  - Age Groups: kids, young_learners, students, adults
 *  - Categories: characters, stories, weapons, places, relationships, values
 *  - Difficulties: easy, medium, hard
 */

const MAHABHARATA_QUESTIONS = """ + json.dumps(questions, indent=2) + """;

// Export for ES modules and browser global script compatibility
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { MAHABHARATA_QUESTIONS };
} else if (typeof window !== 'undefined') {
  window.MAHABHARATA_QUESTIONS = MAHABHARATA_QUESTIONS;
}
"""

with open("js/data/questions.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Successfully written to js/data/questions.js!")
