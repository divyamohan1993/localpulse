// Voice bot intent stubs (MLP — heuristic keyword match; production: LLM intent + Whisper STT)
const intents = {
  emergency: {
    keywords: { en: ['help', 'fire', 'medical', 'ambulance', 'urgent', 'emergency', 'bleeding', 'unconscious'], hi: ['मदद', 'आग', 'एम्बुलेंस', 'चिकित्सा', 'आपातकाल', 'बेहोश'], pa: ['ਮਦਦ', 'ਅੱਗ', 'ਐਂਬੂਲੈਂਸ', 'ਡਾਕਟਰ', 'ਐਮਰਜੈਂਸੀ'], ta: ['உதவி', 'தீ', 'ஆம்புலன்ஸ்', 'மருத்துவம்'], bn: ['সাহায্য', 'আগুন', 'অ্যাম্বুলেন্স', 'জরুরি'] },
    response: {
      en: 'Connecting you to emergency services on 112. Stay on the line. Tell me your nearest landmark.',
      hi: '112 आपातकालीन सेवा से जोड़ रहा हूँ। लाइन पर रहिए। अपना निकटतम landmark बताएँ।',
      pa: '112 ਐਮਰਜੈਂਸੀ ਨਾਲ ਜੋੜ ਰਿਹਾ ਹਾਂ। ਲਾਈਨ ਉੱਤੇ ਰਹੋ। ਆਪਣਾ ਨੇੜਲਾ landmark ਦੱਸੋ।',
      ta: '112 அவசர சேவைக்கு இணைக்கிறேன். வரிசையில் இருங்கள். உங்கள் அருகிலுள்ள landmark-ஐ சொல்லுங்கள்.',
      bn: '112 জরুরি সেবার সাথে যুক্ত করছি. লাইনে থাকুন. আপনার নিকটতম landmark বলুন.'
    }
  },
  shelter: {
    keywords: { en: ['shelter', 'place to stay', 'where to go', 'rest house', 'hostel'], hi: ['आश्रय', 'रहने की जगह', 'कहाँ जाएँ'], pa: ['ਆਸ਼ਰਯ', 'ਰਹਿਣ ਦੀ ਜਗ੍ਹਾ'], ta: ['தங்குமிடம்', 'எங்கே போகலாம்'], bn: ['আশ্রয়', 'থাকার জায়গা'] },
    response: {
      en: '3 shelters open in Solan. Closest: Govt. Sr. Sec. School Solan, capacity 220, 84 occupied. Hot meals and medical available. I am sending the address as SMS now.',
      hi: 'सोलन में 3 आश्रय खुले हैं। सबसे पास: राजकीय वरिष्ठ माध्यमिक विद्यालय सोलन, क्षमता 220, 84 भरे हैं। गर्म भोजन और चिकित्सा। पता SMS पर भेज रहा हूँ।',
      pa: 'ਸੋਲਨ ਵਿੱਚ 3 ਆਸ਼ਰਯ ਖੁੱਲ੍ਹੇ ਹਨ। ਸਭ ਤੋਂ ਨੇੜੇ: ਸਰਕਾਰੀ ਸੀਨੀਅਰ ਸੈਕੰਡਰੀ ਸਕੂਲ ਸੋਲਨ, ਸਮਰੱਥਾ 220, 84 ਭਰੇ। ਪਤਾ SMS ਉੱਤੇ ਭੇਜ ਰਿਹਾ ਹਾਂ।',
      ta: 'சோலானில் 3 தங்குமிடம் உள்ளன. அருகில்: அரசு மேல்நிலைப் பள்ளி சோலான், திறன் 220, 84 நிரப்பப்பட்டுள்ளன. முகவரியை SMS-ல் அனுப்புகிறேன்.',
      bn: 'সোলানে ৩টি আশ্রয় খোলা। কাছেরটি: সরকারি উচ্চ মাধ্যমিক বিদ্যালয় সোলান, ক্ষমতা ২২০, ৮৪ ভর্তি। ঠিকানা SMS পাঠাচ্ছি।'
    }
  },
  road: {
    keywords: { en: ['road', 'highway', 'block', 'traffic', 'closed', 'open'], hi: ['सड़क', 'राजमार्ग', 'बंद', 'ट्रैफिक'], pa: ['ਸੜਕ', 'ਹਾਈਵੇ', 'ਬੰਦ', 'ਟਰੈਫਿਕ'], ta: ['சாலை', 'நெடுஞ்சாலை', 'மூடியது'], bn: ['রাস্তা', 'হাইওয়ে', 'বন্ধ'] },
    response: {
      en: 'NH-5 near Kandaghat is blocked due to landslide. Diversion is via Subathu road. Other major roads in Solan are open.',
      hi: 'कंडाघाट के पास NH-5 भूस्खलन से बंद है। डायवर्जन सुबाथू रोड से। सोलन की अन्य मुख्य सड़कें खुली हैं।',
      pa: 'ਕੰਡਾਘਾਟ ਕੋਲ NH-5 ਜ਼ਮੀਨ ਖਿਸਕਣ ਨਾਲ ਬੰਦ। ਡਾਇਵਰਜ਼ਨ ਸੁਬਾਥੂ ਰੋਡ। ਬਾਕੀ ਮੁੱਖ ਸੜਕਾਂ ਖੁੱਲ੍ਹੀਆਂ।',
      ta: 'கண்டாகட் அருகே NH-5 நிலச்சரிவில் அடைப்பு. சுபாது சாலை வழியாக மாற்றுப்பாதை. சோலானின் பிற முக்கிய சாலைகள் திறந்துள்ளன.',
      bn: 'কান্দাঘাটের কাছে NH-5 ভূমিধসে বন্ধ। সুবাথু রোড দিয়ে ডাইভারশন। সোলানের অন্য প্রধান রাস্তা খোলা।'
    }
  },
  power: {
    keywords: { en: ['power', 'electricity', 'light', 'cut', 'outage'], hi: ['बिजली', 'लाइट', 'कटौती'], pa: ['ਬਿਜਲੀ', 'ਲਾਈਟ', 'ਕੱਟ'], ta: ['மின்சாரம்', 'விளக்கு', 'மின்தடை'], bn: ['বিদ্যুৎ', 'বাতি', 'বিভ্রাট'] },
    response: {
      en: 'Power is out in Anhech and Chambaghat. HPSEBL crew is on site. Restoration expected in about 2 hours.',
      hi: 'अन्हेच और चंबाघाट में बिजली बंद है। HPSEBL टीम मौके पर है। लगभग 2 घंटे में बहाली अपेक्षित।',
      pa: 'ਅਨਹੇਚ ਤੇ ਚੰਬਾਘਾਟ ਵਿੱਚ ਬਿਜਲੀ ਬੰਦ। HPSEBL ਟੀਮ ਮੌਕੇ ਉੱਤੇ। ਲਗਭਗ 2 ਘੰਟੇ ਵਿੱਚ ਮੁੜ ਚਾਲੂ।',
      ta: 'அன்ஹெச் மற்றும் சம்பாகட்டில் மின்தடை. HPSEBL குழு இடத்தில். சுமார் 2 மணியில் மீட்பு.',
      bn: 'অন্হেচ ও চম্বাঘাটে বিদ্যুৎ বন্ধ। HPSEBL দল ঘটনাস্থলে। প্রায় ২ ঘণ্টায় পুনরুদ্ধার।'
    }
  },
  water: {
    keywords: { en: ['water', 'tanker', 'drinking'], hi: ['पानी', 'टैंकर'], pa: ['ਪਾਣੀ', 'ਟੈਂਕਰ'], ta: ['தண்ணீர்', 'டேங்கர்'], bn: ['পানি', 'ট্যাঙ্কার'] },
    response: {
      en: 'Water tanker at Mall Road, every 2 hours, free, no ID needed. Bring your own containers.',
      hi: 'मॉल रोड पर हर 2 घंटे में पानी का टैंकर, मुफ्त, ID की जरूरत नहीं। अपने बर्तन लाएँ।',
      pa: 'ਮਾਲ ਰੋਡ ਉੱਤੇ ਹਰ 2 ਘੰਟੇ ਪਾਣੀ ਦਾ ਟੈਂਕਰ, ਮੁਫ਼ਤ, ID ਬਿਨਾਂ। ਆਪਣੇ ਭਾਂਡੇ ਲਿਆਓ।',
      ta: 'மால் ரோட்டில் ஒவ்வொரு 2 மணிக்கும் இலவச தண்ணீர் டேங்கர். உங்கள் பாத்திரம் கொண்டு வாருங்கள்.',
      bn: 'মল রোডে প্রতি ২ ঘণ্টায় বিনামূল্যে পানির ট্যাঙ্কার। নিজের পাত্র আনুন।'
    }
  },
  medical: {
    keywords: { en: ['medical', 'doctor', 'medicine', 'insulin', 'first aid'], hi: ['डॉक्टर', 'दवा', 'चिकित्सा', 'इंसुलिन'], pa: ['ਡਾਕਟਰ', 'ਦਵਾਈ', 'ਡਾਕਟਰੀ'], ta: ['மருத்துவம்', 'மருந்து'], bn: ['চিকিৎসা', 'ডাক্তার', 'ওষুধ'] },
    response: {
      en: 'Mobile medical camp at Rajgarh PHC has doctors, ambulance, basic medicines, insulin and ORS in stock.',
      hi: 'राजगढ़ PHC पर मोबाइल मेडिकल कैंप में डॉक्टर, एम्बुलेंस, बुनियादी दवाएँ, इंसुलिन और ORS उपलब्ध।',
      pa: 'ਰਾਜਗੜ੍ਹ PHC ਉੱਤੇ ਮੋਬਾਈਲ ਡਾਕਟਰੀ ਕੈਂਪ ਵਿੱਚ ਡਾਕਟਰ, ਐਂਬੂਲੈਂਸ, ਦਵਾਈਆਂ, ਇਨਸੁਲਿਨ ਤੇ ORS ਉਪਲਬਧ।',
      ta: 'ராஜ்கட் PHC-யில் நகரும் மருத்துவ முகாமில் மருத்துவர்கள், ஆம்புலன்ஸ், அடிப்படை மருந்துகள், இன்சுலின் + ORS கையிருப்பில்.',
      bn: 'রাজগড় PHC-তে মোবাইল চিকিৎসা শিবিরে ডাক্তার, অ্যাম্বুলেন্স, ওষুধ, ইনসুলিন ও ORS মজুদ।'
    }
  },
  fallback: {
    keywords: {},
    response: {
      en: "I didn't catch that. You can ask me about roads, shelters, power, water, or medical help. Or say 'emergency' to connect to 112.",
      hi: 'मुझे समझ नहीं आया। आप मुझसे सड़क, आश्रय, बिजली, पानी या चिकित्सा के बारे में पूछ सकते हैं। या 112 के लिए "आपातकाल" कहें।',
      pa: 'ਸਮਝ ਨਹੀਂ ਆਇਆ। ਤੁਸੀਂ ਸੜਕ, ਆਸ਼ਰਯ, ਬਿਜਲੀ, ਪਾਣੀ ਜਾਂ ਡਾਕਟਰੀ ਬਾਰੇ ਪੁੱਛ ਸਕਦੇ ਹੋ। ਜਾਂ 112 ਲਈ "ਐਮਰਜੈਂਸੀ" ਕਹੋ।',
      ta: 'புரியவில்லை. சாலை, தங்குமிடம், மின்சாரம், தண்ணீர் அல்லது மருத்துவம் பற்றி கேளுங்கள். அல்லது 112-க்கு "அவசரம்" என்று சொல்லுங்கள்.',
      bn: 'বুঝতে পারিনি। রাস্তা, আশ্রয়, বিদ্যুৎ, পানি বা চিকিৎসা সম্পর্কে জিজ্ঞাসা করতে পারেন। বা 112-এর জন্য "জরুরি" বলুন।'
    }
  }
};

function classify(text, lang = 'en') {
  if (!text) return 'fallback';
  const t = text.toLowerCase();
  const order = ['emergency', 'shelter', 'road', 'power', 'water', 'medical'];
  for (const intent of order) {
    const kws = (intents[intent].keywords[lang] || []).concat(intents[intent].keywords.en || []);
    for (const kw of kws) {
      if (t.includes(kw.toLowerCase())) return intent;
    }
  }
  return 'fallback';
}

function respond(text, lang = 'en') {
  const intent = classify(text, lang);
  const response = intents[intent].response[lang] || intents[intent].response.en;
  return { intent, response, lang, ts: Date.now() };
}

module.exports = { intents, classify, respond };
