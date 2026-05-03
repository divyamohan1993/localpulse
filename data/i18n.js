// Server-side i18n dictionary. Mirrors public/js/i18n.js for SSR-safe pages.
const dict = {
  en: {
    appName: 'LocalPulse',
    tagline: 'Verified status for your town. Built for slow phones, bad internet, small towns.',
    nav: { dashboard: 'Dashboard', responder: 'Responder', voice: 'Voice', pitch: 'Pitch', report: 'Report' },
    status: { online: 'Live', stale: 'Cached', offline: 'Offline' },
    cta: { report: 'Report an issue', call: 'Call our voice line' },
    summaryTitle: 'Last hour summary',
    incidents: 'Incidents',
    shelters: 'Open shelters',
    severity: { high: 'High', medium: 'Medium', low: 'Low', info: 'Info' },
    cat: { road: 'Roads', shelter: 'Shelter', power: 'Power', water: 'Water', medical: 'Medical', rumor: 'Rumor flagged' },
    trust: 'Trust',
    sources: 'sources',
    verified: 'verified',
    updated: 'updated',
    minAgo: 'min ago',
    privacy: 'No login. No tracking. Data stays in India.',
    voiceLine: 'Voice helpline: 1800-LOCAL-PULSE (demo)'
  },
  hi: {
    appName: 'LocalPulse',
    tagline: 'अपने शहर के लिए सत्यापित स्थिति। धीमे फ़ोन, खराब इंटरनेट, छोटे शहरों के लिए।',
    nav: { dashboard: 'डैशबोर्ड', responder: 'रिस्पॉन्डर', voice: 'वॉइस', pitch: 'पिच', report: 'रिपोर्ट' },
    status: { online: 'लाइव', stale: 'कैश्ड', offline: 'ऑफ़लाइन' },
    cta: { report: 'समस्या बताएँ', call: 'वॉइस लाइन पर कॉल करें' },
    summaryTitle: 'पिछले एक घंटे का सारांश',
    incidents: 'घटनाएँ',
    shelters: 'खुले आश्रय',
    severity: { high: 'उच्च', medium: 'मध्यम', low: 'कम', info: 'सूचना' },
    cat: { road: 'सड़कें', shelter: 'आश्रय', power: 'बिजली', water: 'पानी', medical: 'चिकित्सा', rumor: 'अफवाह' },
    trust: 'विश्वास',
    sources: 'स्रोत',
    verified: 'सत्यापित',
    updated: 'अद्यतन',
    minAgo: 'मिनट पहले',
    privacy: 'कोई लॉगिन नहीं. कोई ट्रैकिंग नहीं. डेटा भारत में रहता है.',
    voiceLine: 'वॉइस हेल्पलाइन: 1800-LOCAL-PULSE (डेमो)'
  },
  pa: {
    appName: 'LocalPulse',
    tagline: 'ਆਪਣੇ ਸ਼ਹਿਰ ਲਈ ਪ੍ਰਮਾਣਿਤ ਜਾਣਕਾਰੀ। ਹੌਲੀ ਫ਼ੋਨ ਤੇ ਮਾੜੇ ਇੰਟਰਨੈੱਟ ਲਈ।',
    nav: { dashboard: 'ਡੈਸ਼ਬੋਰਡ', responder: 'ਰਿਸਪਾਂਡਰ', voice: 'ਆਵਾਜ਼', pitch: 'ਪਿੱਚ', report: 'ਰਿਪੋਰਟ' },
    status: { online: 'ਲਾਈਵ', stale: 'ਕੈਸ਼', offline: 'ਆਫ਼ਲਾਈਨ' },
    cta: { report: 'ਸਮੱਸਿਆ ਦੱਸੋ', call: 'ਫ਼ੋਨ ਲਾਈਨ ਉੱਤੇ ਕਾਲ ਕਰੋ' },
    summaryTitle: 'ਪਿਛਲੇ ਘੰਟੇ ਦਾ ਸਾਰ',
    incidents: 'ਘਟਨਾਵਾਂ',
    shelters: 'ਖੁੱਲ੍ਹੇ ਆਸ਼ਰਯ',
    severity: { high: 'ਉੱਚ', medium: 'ਮੱਧਮ', low: 'ਘੱਟ', info: 'ਸੂਚਨਾ' },
    cat: { road: 'ਸੜਕਾਂ', shelter: 'ਆਸ਼ਰਯ', power: 'ਬਿਜਲੀ', water: 'ਪਾਣੀ', medical: 'ਡਾਕਟਰੀ', rumor: 'ਅਫ਼ਵਾਹ' },
    trust: 'ਭਰੋਸਾ',
    sources: 'ਸਰੋਤ',
    verified: 'ਪ੍ਰਮਾਣਿਤ',
    updated: 'ਅੱਪਡੇਟ',
    minAgo: 'ਮਿੰਟ ਪਹਿਲਾਂ',
    privacy: 'ਕੋਈ ਲਾਗਇਨ ਨਹੀਂ। ਕੋਈ ਟਰੈਕਿੰਗ ਨਹੀਂ। ਡਾਟਾ ਭਾਰਤ ਵਿੱਚ ਰਹਿੰਦਾ ਹੈ।',
    voiceLine: 'ਫ਼ੋਨ ਲਾਈਨ: 1800-LOCAL-PULSE (ਡੈਮੋ)'
  },
  ta: {
    appName: 'LocalPulse',
    tagline: 'உங்கள் நகரத்திற்கு சரிபார்க்கப்பட்ட நிலை. மெதுவான ஃபோன், மோசமான இணையத்திற்கு.',
    nav: { dashboard: 'டாஷ்போர்டு', responder: 'பதிலளிப்பவர்', voice: 'குரல்', pitch: 'பிட்ச்', report: 'அறிக்கை' },
    status: { online: 'நேரலை', stale: 'கேஷ்', offline: 'ஆஃப்லைன்' },
    cta: { report: 'சிக்கலை தெரிவிக்கவும்', call: 'குரல் வழியாக அழைக்கவும்' },
    summaryTitle: 'கடந்த மணி நேர சுருக்கம்',
    incidents: 'சம்பவங்கள்',
    shelters: 'திறந்த தங்குமிடம்',
    severity: { high: 'அதிகம்', medium: 'நடுத்தர', low: 'குறைவு', info: 'தகவல்' },
    cat: { road: 'சாலைகள்', shelter: 'தங்குமிடம்', power: 'மின்சாரம்', water: 'தண்ணீர்', medical: 'மருத்துவம்', rumor: 'வதந்தி' },
    trust: 'நம்பிக்கை',
    sources: 'ஆதாரங்கள்',
    verified: 'சரிபார்க்கப்பட்டது',
    updated: 'புதுப்பிக்கப்பட்டது',
    minAgo: 'நிமிடங்கள் முன்',
    privacy: 'உள்நுழைவு இல்லை. கண்காணிப்பு இல்லை. தரவு இந்தியாவில் தங்கும்.',
    voiceLine: 'குரல் உதவி: 1800-LOCAL-PULSE (டெமோ)'
  },
  bn: {
    appName: 'LocalPulse',
    tagline: 'আপনার শহরের জন্য যাচাইকৃত তথ্য। ধীর ফোন, দুর্বল ইন্টারনেটের জন্য।',
    nav: { dashboard: 'ড্যাশবোর্ড', responder: 'রেসপন্ডার', voice: 'ভয়েস', pitch: 'পিচ', report: 'রিপোর্ট' },
    status: { online: 'লাইভ', stale: 'ক্যাশ', offline: 'অফলাইন' },
    cta: { report: 'সমস্যা জানান', call: 'ভয়েস লাইনে কল করুন' },
    summaryTitle: 'গত এক ঘণ্টার সারাংশ',
    incidents: 'ঘটনা',
    shelters: 'খোলা আশ্রয়',
    severity: { high: 'উচ্চ', medium: 'মাঝারি', low: 'নিম্ন', info: 'তথ্য' },
    cat: { road: 'রাস্তা', shelter: 'আশ্রয়', power: 'বিদ্যুৎ', water: 'পানি', medical: 'চিকিৎসা', rumor: 'গুজব' },
    trust: 'বিশ্বাস',
    sources: 'উৎস',
    verified: 'যাচাইকৃত',
    updated: 'আপডেট',
    minAgo: 'মিনিট আগে',
    privacy: 'কোনো লগইন নেই. কোনো ট্র্যাকিং নেই. ডেটা ভারতে থাকে.',
    voiceLine: 'ভয়েস হেল্পলাইন: 1800-LOCAL-PULSE (ডেমো)'
  }
};

const SUPPORTED = ['en', 'hi', 'pa', 'ta', 'bn'];
const DEFAULT_LANG = 'en';

function pickLang(req) {
  const q = (req.query && req.query.lang) || '';
  if (SUPPORTED.includes(q)) return q;
  const al = (req.headers['accept-language'] || '').toLowerCase();
  for (const code of SUPPORTED) if (al.includes(code)) return code;
  return DEFAULT_LANG;
}

module.exports = { dict, SUPPORTED, DEFAULT_LANG, pickLang };
