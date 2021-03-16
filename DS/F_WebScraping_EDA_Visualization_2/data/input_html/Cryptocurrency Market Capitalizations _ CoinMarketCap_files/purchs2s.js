var PURCHS2S_VERSION="1.0.21",purchs2s=purchs2s||{};purchs2s.cmd=purchs2s.cmd||[];purchs2s.timing={};purchs2s.timing.adunits={};purchs2s.timing.start=(new Date).getTime();purchs2sutils={};purchs2sutils.status={};function uuidv4(){return"xxxxxxxxxxxx4xxxyxxxxxxxxxxxxxxx".replace(/[xy]/g,function(a){var b=Math.random()*16|0;a=a=="x"?b:b&3|8;return a.toString(16)})}var defuuid=uuidv4();
(function(a){function b(){if(!e){e=true;for(var a=0;a<d.length;a++)d[a].fn.call(window,d[a].ctx);d=[]}}function c(){if(document.readyState==="complete")b()}baseObj=window;var d=[],e=false,f=false;baseObj[a]=function(a,k){if(e){setTimeout(function(){a(k)},1);return}else d.push({fn:a,ctx:k});if(document.readyState==="complete"||!document.attachEvent&&document.readyState==="interactive")setTimeout(b,1);else if(!f){if(document.addEventListener){document.addEventListener("DOMContentLoaded",b,false);window.addEventListener("load",
b,false)}else{document.attachEvent("onreadystatechange",c);window.attachEvent("onload",b)}f=true}}})("tmntag_ready");
purchs2sutils.processBidResponseTimeout=function(a,b){if(purchs2s.bidResponseProcessed)return;purchs2s.bidResponseProcessed=true;purchs2sutils.status.bidRequestTimeout=true;if(!a)googletag.cmd.push(function(){googletag.pubads().refresh()});else{a=googletag.pubads().getSlots();if(typeof b!="undefined"&&b&&a){for(var c=[],d=0;d<b.length;d++)for(var e=0;e<a.length;e++){var f=a[e],g=f.getSlotElementId();if(g===b[d])c.push(f)}if(c.length>0)googletag.pubads().refresh(c)}else if(typeof b=="undefined"||!b)googletag.pubads().refresh()}if(purchs2s.timeoutHandler){purchs2sutils.log("Timeout after "+
purchs2sutils.timeout()+" ms");purchs2s.timeoutHandler()}};purchs2sutils.timeout=function(){return purchs2s.timeout?purchs2s.timeout:500};purchs2sutils.log=function(a){};purchs2s.setPersonalizedAdsMode=function(a){this.mode=a};purchs2s.getPersonalizedAdsMode=function(){return this.mode||"allowed"};purchs2sutils._formateMacromapList=function(a){if(!a||a.indexOf("$")===0)return[];return a.split("|")};
purchs2sutils._currentDomainIsInList=function(a){a=a.find(function(a){return document.location.hostname.indexOf(a)!==-1});return!!a};(function(){var a=purchs2sutils._formateMacromapList("anandtech.com|coinranking.com|dignifyed.com|laptopmag.com|livescience.com|newsarama.com|shopsavvy.com|space.com|tomsguide.com|tomshardware.com|tomsitpro.com|toptenreviews.com");purchs2s.setPersonalizedAdsMode("allowed");if(window.gdprUser)if(purchs2sutils._currentDomainIsInList(a))purchs2s.setPersonalizedAdsMode("managed");else purchs2s.setPersonalizedAdsMode("blocked")})();
purchs2sutils.setup=function(a,b){for(var c=function(a,b){var c={};if(a)purchs2s.f=1;c.f=purchs2s.f;c.p=a?"":purchs2s.p;c.s=purchs2s.s;c.g=purchs2s.g;c.l=purchs2s.l;c.tt=purchs2s.tt;c.tt=c.tt.replace(/'|;|quot;|39;|&amp;|&|#|\r\n|\r|\n|\t|\f|\%0A|\"|\%22|\%5C|\%23|\%26|\%26|\%09/gm,"");c.fs=purchs2s.fs;c.rtb=purchs2s.rtb;{var d=b;a=purchs2s.a||[];b=[];if(!d||!d.length)b=a;else if(a){var e=[];if(!(d instanceof Array))e.push(d);else e=d;for(var d=0,k=a.length;d<k;d++){var f=a[d];if(f&&f.d&&e.indexOf(f.d)>
-1)b.push(f)}}a=b}c.a=a;c.t=purchs2sutils.timestamp();c.tz=Math.round((new Date).getTimezoneOffset());c.r=purchs2sutils.clientDim();c.pam=purchs2s.getPersonalizedAdsMode();return JSON.stringify(c).replace(/'|&|#/g,"")},d=function(){for(var a=0;a<document.scripts.length;a++){var b=document.scripts[a],c=b.src.indexOf("purchs2s.js");if(c>0)return b.src.substring(0,c)}return"http://ads.servebom.com/"},e=googletag.pubads().getSlots(),f=0;e&&f<e.length;f++){for(var g=e[f],k=g.getSizes(),m=[],n=0;k&&n<k.length;n++)m.push([k[n].getWidth(),
k[n].getHeight()]);purchs2s.adunit({account:g.getAdUnitPath(),div:g.getSlotElementId(),sizes:m})}e=Math.floor(Math.random()*11E3);d=d();c="r="+e+"&o="+c(a,b)+"&fmt=jsonp";if(typeof defuuid!="undefined")c+="&uuid="+defuuid;c=d+"purchs2stag.js?v=s2s&"+c;purchs2s.timing.bidRequestSent=(new Date).getTime();purchs2s.bidResponseProcessed=false;setTimeout(purchs2sutils.processBidResponseTimeout,purchs2sutils.timeout()+500,a,b);purchs2sutils.loadScript(c)};
purchs2sutils.processBidResponse=function(a){if(a.isNonPersonalizedAds)googletag.cmd.push(function(){googletag.pubads().setRequestNonPersonalizedAds(1)});purchs2s.timing.bidResponseReady=(new Date).getTime()-purchs2s.timing.bidRequestSent;purchs2sutils.log("purchs2s.timing.bidResponseReady "+purchs2s.timing.bidResponseReady);var b=function(a){a=a.targeting;if(typeof a!="undefined"&&a)for(var b in a)googletag.pubads().setTargeting(b,a[b])},c=function(a){a=a.exp;if(typeof a!="undefined"&&a)googletag.pubads().setTargeting("_ex",
e(a))},d=function(a){for(var b=googletag.pubads().getSlots(),c=[],d=0;typeof a!="undefined"&&a&&b&&d<b.length;d++){var e=b[d],f=e.getSlotElementId(),k=a.bids,g=false;if(typeof k!="undefined"&&k)for(var p=0;p<k.length;p++){var l=k[p];if(l.divid===f){c.push(e);if("1"===l.brdid||"1"===l.bdrid)continue;purchs2s.timing.adunits[f]={};purchs2s.timing.adunits[f].received_bid=(new Date).getTime()-purchs2s.timing.bidRequestSent;e.setTargeting("adunit",l.divid);e.setTargeting("_bd","bid");e.setTargeting("_cp",
l.price);e.setTargeting("_pl",l.bucket);e.setTargeting("_br",l.bidder);e.setTargeting("_wb",l.id);e.setTargeting("_sz",l.size_code);if(l.dealid)e.setTargeting("_pdid",l.dealid);g=true;break}}if(!g){if(purchs2s.passbackHandler){purchs2sutils.log("Passback for adunit "+f);purchs2s.passbackHandler(f)}}else if(purchs2s.fillHandler){purchs2sutils.log("Bid available for adunit "+f);purchs2s.fillHandler(f)}}return c},e=function(a){var b="";if(typeof a!="undefined"&&a)for(var c=0;c<a.length;c++){if(c==0)b+=
"|";b+=a[c]+"|"}return b},f=function(a,b){purchs2sutils.evalJSON(a.content);if(purchs2s.pixelHandler){purchs2sutils.log("Pixel rendered index:"+b+", campaign:"+a.campaign);purchs2s.pixelHandler(b,a.campaign)}},g=function(a){if(!a.refresh&&typeof a.pixels!="undefined"&&a.pixels)a.pixels.sort(function(a,b){return(b.prepend?1:0)-(a.prepend?1:0)}).forEach(function(a,b){if(a&&!a.donotrender&&a.content)if(a.onready)tmntag_ready(function(){f(a,b)});else f(a,b)});purchs2sutils.status.pixelsProcessed=true};
if(purchs2s.bidResponseProcessed)return;purchs2s.bidResponseProcessed=true;purchs2sutils.status.bidRequestTimeout=false;purchs2s.bidResponse=a;if(typeof a=="undefined"||!a){googletag.cmd.push(function(){googletag.pubads().refresh()});if(purchs2s.timeoutHandler){purchs2sutils.log("Timeout");purchs2s.timeoutHandler()}return}g(a);c(a);b(a);b=d(a);if(!a.refresh)googletag.cmd.push(function(){googletag.pubads().refresh()});else googletag.pubads().refresh(b);purchs2sutils.status.bidRequestProcessed=true};
purchs2sutils.evalJSON=function(a){try{eval(a)}catch(b){console&&console.error&&console.error(b)}};purchs2sutils.getAdUnit=function(a){for(var b=0;b<purchs2s.a.length;b++)if(purchs2s.a[b].d===a)return purchs2s.a[b];return false};
purchs2sutils.supportsFlash=function(){var a=1;try{if(navigator.mimeTypes&&navigator.mimeTypes.length>0){var b=navigator.mimeTypes["application/x-shockwave-flash"];if(b&&b.enabledPlugin)a=1}else if(typeof ActiveXObject!="undefined")try{new ActiveXObject("ShockwaveFlash.ShockwaveFlash.1");a=1}catch(c){}}catch(c){console&&console.error&&console.error(exception)}return a};
purchs2sutils.clientDim=function(){try{w=document.documentElement.clientWidth||document.body.clientWidth||window.innerWidth;h=document.documentElement.clientHeight||document.body.clientHeight||window.innerHeight;return w+"x"+h}catch(a){}};purchs2sutils.topLocation=function(){try{return window.context&&window.context.location&&window.context.location.href?window.context.location.href:window.top.document.location.href}catch(a){return window.document.referrer}};
purchs2sutils.timestamp=function(){var a=new Date,b=function(a){return a<=9?"0"+a:""+a},c=a.getDate(),d=a.getFullYear(),e=a.getMonth()+1,f=a.getHours(),g=a.getMinutes(),k=a.getSeconds();a.getMilliseconds();return""+d+"-"+b(e)+"-"+b(c)+" "+b(f)+":"+b(g)+":"+b(k)};purchs2s.a=[];purchs2s.l=encodeURIComponent(purchs2sutils.topLocation().replace("%",""));purchs2s.tt=encodeURIComponent(document.title);purchs2s.t=purchs2sutils.timestamp();purchs2s.tz=Math.round((new Date).getTimezoneOffset());
purchs2s.r=purchs2sutils.clientDim();purchs2s.fs=purchs2sutils.supportsFlash();purchs2sutils.loadScript=function(a){var b=document.createElement("script");b.async=true;b.src=a;a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(b,a)};purchs2s.location=function(a){purchs2sutils.log("Location set to "+a);purchs2s.l=encodeURIComponent(a)};
purchs2s.adunit=function(a){var b=purchs2sutils.getAdUnit(a.div)||{};if(a.account)b.s=a.account;else if(purchs2s.s)b.s=purchs2s.s;if(a.sizes)b.z=a.sizes;if(a.div)b.d=a.div;if(a.targeting)b.g=a.targeting;else b.g={};if(a.companion)b.c=a.companion;if(a.div)for(var c=purchs2s.a,d=a.div,e=c.length-1;e>=0;e--){var f=c[e];if(f.d&&f.d===d)c.splice(e,1)}if(a.sizeMapping)b.sm=a.sizeMapping;if(a.rtb)b.rtb=a.rtb;purchs2s.a.push(b);return b};purchs2s.rtb=function(a){purchs2s.rtb=a};
purchs2s.setup=function(){purchs2sutils.log("purchs2s.setup called");purchs2sutils.setup()};purchs2s.render=function(a,b){return tmntag_render(a,b)};purchs2s.sizeMapping=function(a){var b=[];return{divid:a,addSize:function(a,d){b.push([a,d]);return this},build:function(){var c=[];if(googletag){for(var d=googletag.sizeMapping(),e=0;e<b.length;e++)d.addSize(b[e][0],b[e][1]);c=d.build();purchs2s.cmd.push(function(){purchs2s.adunit({div:a,sizeMapping:c})})}return c}}};
tmntag_render=function(a,b){purchs2sutils.log("purchs2s.render called for ad unit "+b);var c=false;if(typeof purchs2s.bidResponse!="undefined"&&purchs2s.bidResponse&&typeof purchs2s.bidResponse.bids!="undefined"&&purchs2s.bidResponse.bids){var d=purchs2s.bidResponse.bids;if(typeof d!="undefined"&&d)for(var e=0;e<d.length;e++){var f=d[e];if(f.divid===b){var d=f.adm,g=1,k=1;if(f.size){if(f.size.w)g=f.size.w;if(f.size.h)k=f.size.h}if(typeof d!="undefined"&&d!=null&&d){purchs2s.timing.adunits[b].rendered=
(new Date).getTime()-purchs2s.timing.start;d=d.replace(/'\r\n|\r|\n/gm,"");if((typeof confiantWrap=="function"||typeof confiantWrapWithCallback==="function")&&CONFIANT_WRAPPER_ID){var c=purchs2sutils.bidderName(f),m="purch_"+c,c={ad:d,bidder:m,size:g+"x"+k,cpm:f.price||0};if(typeof confiantWrapWithCallback==="function"){d=function(a,b,c,d,e,q){tmntag_triggerEvent("CB",{bdrid:f.bdrid||0,tid:m+":"+g+"x"+k,crid:b,ad:a,cp:q.prebid.cpm,id:window.requestid})};if(!confiantWrapWithCallback(a,c,"clarium.global.ssl.fastly.net",
CONFIANT_WRAPPER_ID,d)){a.write(c.ad);a.close()}}else if(!confiantWrap(a,c.ad,c.bidder,c.size,"clarium.global.ssl.fastly.net",CONFIANT_WRAPPER_ID)){a.write(d);a.close()}}else{a.write(d);a.close()}c=true;d=googletag.pubads().getSlots();for(e=0;d&&e<d.length;e++)if((slot=d[e])&&b===slot.getSlotElementId()){slot.setTargeting("_bd","none");break}if(a.defaultView&&a.defaultView.frameElement){d=g+"px";e=k+"px";a.defaultView.frameElement.width=d;a.defaultView.frameElement.height=e;if(top!==self&&self&&self.frameElement){self.frameElement.width=
d;self.frameElement.height=e}}}break}}}if(c)if(purchs2s.renderHandler){purchs2sutils.log("Ad Rendered for ad unit "+b);purchs2s.renderHandler(b)}return c};
tmntag_triggerEvent=function(a,b){var c="";if(b)for(var d in b){if(c!="")c+="&";if(b[d].indexOf("$")==-1)c+=d+"="+b[d]}d=Math.floor(Math.random()*11E3);c="t="+a+"&r="+d+"&"+c;if(a=="CP"&&b&&b.ts&&b.ts.indexOf("$")==-1)c=c+"&tm_alt="+(Date.now()-b.ts);a=document.createElement("script");a.src="//ads.servebom.com/event.js?"+c;c=document.getElementsByTagName("script")[0];c.parentNode.insertBefore(a,c)};
purchs2s.refresh=function(a){purchs2sutils.log("purchs2s.refresh called for ad unit(s) "+a);purchs2sutils.setup(true,a)};purchs2s.cmd.executeCommands=function(){for(;i=purchs2s.cmd.shift();)if(typeof i==="function")i()};purchs2s.cmd.push=function(a){purchs2s.cmd.executeCommands();if(typeof a==="function")a()};purchs2s.cmd.pushDefined=true;var purchs2s_checkCommands=function(){if(!purchs2s.cmd.pushDefined)setTimeout(purchs2s_checkCommands,100);else purchs2s.cmd.executeCommands()};purchs2s_checkCommands();
purchs2s.apiReady=true;
purchs2s.debug=function(){console.log("--------------------- PURCH S2S DEBUG ---------------------");var a={};a.bidResponse=purchs2s.bidResponse;a.timing=purchs2s.timing;a.googletag=typeof googletag!="undefined"?googletag:"none";a.purchs2s=purchs2s;a.googleSlots=typeof googletag!="undefined"?googletag.pubads().getSlots():"none";a.pageLoation=purchs2sutils.topLocation();a.bidResponseProcessed=purchs2s.bidResponseProcessed;a.bidRequestTimeout=purchs2sutils.status.bidRequestTimeout;a.status=purchs2sutils.status;
if(googletag){var b=googletag.pubads().getSlots(),b=b.map(function(a){a=a.getSlotElementId();var b=document.getElementById(a);if(!b)ret={Message:"Ad Slot declared in GPT, but NO DIV found on page",DIV:a,Type:"BAD !"};else ret={Message:"Checked",DIV:a,Type:"GOOD"};return ret});if(console.table){console.log("TAGS CHECK:");console.table(b)}a.tagchecks=b}if(a.bidRequestTimeout)console.log("BID REQUEST TIMED OUT");console.log("BIDS:");if(purchs2s.bidResponse&&purchs2s.bidResponse.bids)console.table(purchs2s.bidResponse.bids);
console.log("-----------------------------------------------------------");return a};
purchs2sutils.bidderName=function(a){var b="NA";if(a)if(a.bidderName)b=a.bidderName;else{b={CAXS:"Index-Simulator",15108529:"Index",60822169:"Pubmatic",14481529:"Amazon",84300529:"Yieldbot",87260329:"Sonobi",85099489:"Yellowhammer",95587969:"Bidtellect",103230529:"Triplelift",103229929:"Nativeads",103229809:"Distroscale",103230049:"Appnexus",103229569:"AOL",103229089:"C1X",103229449:"Rubicon",103229329:"Searchlinks",103229689:"Pulsepoint",103229209:"Purch",131060089:"OpenX",131059969:"Sovrn",131059849:"BRealtime",
103228969:"Districtm",131059129:"Powerlinks",131059369:"Facebook",167403649:"Tremor",167403889:"Defymedia",103230649:"Wideorbit",131059609:"Adblade",167404249:"Inneractive",131059489:"Sekindo",167405209:"Mediamath"};b=b[a.bidder]||a.bidder}return b};purchs2sutils.cookies={};purchs2sutils.cookies.get=function(a){var b="; "+document.cookie;a=b.split("; "+a+"=");if(a.length===2)return a.pop().split(";").shift()};
purchs2sutils.cookies.getAll=function(){return document.cookie.split("; ").reduce(function(a,b){var c=b.indexOf("=");a[b.substr(0,c)]=b.substr(c+1);return a},{})};purchs2sutils.cookies.set=function(a,b,c){var d=new Date;d.setTime(d.getTime()+c*1E3);c="expires="+d.toUTCString();document.cookie=a+"="+b+";"+c+";path=/"};purchs2sutils._iabVendorIdMapping={11:185,"23_25_26_29_33":32,22:69,9:104,24:13,14:28,5:76,19:52,36:24,45:76,17:81,2:10,44:277,46:76,27:236};
purchs2sutils._waitForCMP=function(a){if(typeof window.__cmp!=="function")return window.setTimeout(function(){purchs2sutils._waitForCMP(a)},100);return a()};
purchs2s_executeWithGDPRConsent=function(a,b){if(arguments.length===1)b=a;switch(purchs2s.getPersonalizedAdsMode()){case "blocked":return;case "allowed":return b();case "managed":var c=purchs2sutils._formateMacromapList("phonandroid.com|frandroid.com|generation-nt.com|gamergen.com|numerama.com|driverscloud.com|hitek.fr|tomsguide.fr|tomshardware.fr");if(purchs2sutils._currentDomainIsInList(c))return b();else purchs2sutils._waitForCMP(function(){window.__cmp("addEventListener","cmpReady",function(){window.__cmp("getVendorConsents",[a],function(c){if(c.vendorConsents&&c.vendorConsents[a])return b()})})})}};
var userSyncPixels={};userSyncPixels._cookiesMap=purchs2sutils.cookies.getAll();userSyncPixels.create=function(a,b,c,d){purchs2s_executeWithGDPRConsent(purchs2sutils._iabVendorIdMapping[a],function(){if(!userSyncPixels._cookiesMap["usp."+a]){var b=purchs2sutils._formateMacromapList(b);if(purchs2sutils._currentDomainIsInList(b)===c)d()}purchs2sutils.cookies.set("usp."+a,1,"604800");userSyncPixels._cookiesMap["usp."+a]=1})};
function purch_history(a){a.pvLoggingDisabled=true;a.pageHistory={};a.pageHistory[window.location.pathname]=1;(function(a){var b=a.replaceState;a.replaceState=function(c,d,g){if(typeof a.onreplacestate=="function"&&window.location.pathname!=g)a.onreplacestate(c,d,g);return b.apply(a,arguments)};var d=a.pushState;a.pushState=function(b,c,g){if(typeof a.onpushstate=="function"&&window.location.pathname!=g)a.onpushstate(b,c,g);return d.apply(a,arguments)}})(window.history);history.onreplacestate=history.onpushstate=
function(b,c,d){if(!a.onPageChangedDisabled){{b=d;if(!a.pageHistory[b]){a.pageHistory[b]=1;purch_history_onNewPage(b)}}}};window.purch_history_onNewPage=function(b){if(!a.pvLoggingDisabled)tmntag_triggerEvent("PV",{ep:encodeURIComponent(b)})}}purch_history(purchs2s);try {
tmntag_ready(function() {

userSyncPixels._fragment=document.createElement("div");

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create("23_25_26_29_33","buyerzone.com|businessnewsdaily.com",false,function(){var a=document.createElement("iframe"),c=Math.floor(Math.random()*11E3);a.style.display="none";var b=document.location.protocol==="http:"?"http":"https";a.defer=true;a.src=b+"://ib.adnxs.com/getuid?"+b+":%2F%2Fads.servebom.com%2Fpartner%3Fcb%3D"+c+"%26svc%3Dus%26id%3D23%2C25%2C26%2C29%26uid%3D$UID";userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

function requestToken(){var a=document.getElementById(frameId);a.contentWindow.postMessage("GET_FB_TOKEN_198782813737","https://www.facebook.com")}function receiveFBToken(a){if(a.origin.indexOf("https://www.facebook.com")!==-1){var b="; expires="+a.data.expAfter;a=JSON.parse(a.data);document.cookie="up_28="+encodeURIComponent(a.fbToken)+b+"; path=/"}}
if(!window.gdprUser){var frameId="fb_iframe";if(typeof window.INSTART==="undefined"){try{var fbIframe=document.createElement("iframe");fbIframe.id=frameId;fbIframe.width="0";fbIframe.height="0";fbIframe.frameBorder="0";fbIframe.src="https://www.facebook.com/audiencenetwork/token/v1/";document.body.appendChild(fbIframe);fbIframe.onload=function(){requestToken()}}catch(a){console.error(a)}window.addEventListener("message",receiveFBToken,false)}};

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create("51_52_53_54","buyerzone.com|businessnewsdaily.com",false,function(){var a=document.createElement("span"),c=Math.floor(Math.random()*11E3);a.style.display="none";var d=document.location.protocol==="https:"?"https":"http",b=document.createElement("iframe");b.style.display="none";b.src="//sync.mathtag.com/sync/img?mt_exid=66&redir="+encodeURIComponent(d+"://ads.servebom.com/partner?cb="+c+"&svc=us&id=51%2C52%2C53%2C54&uid=[MM_UUID]");a.appendChild(b);userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create("22","buyerzone.com|businessnewsdaily.com",false,function(){var a=document.createElement("span"),b=Math.floor(Math.random()*11E3);a.style.display="none";var c=document.location.protocol==="https:"?"https":"http";a.innerHTML='<iframe style="display:none" src="//us-u.openx.net/w/1.0/cm?id=de2d90e5-4d26-4c8c-a342-3edcde51fdb1&ph=25af9286-f23b-4b02-abcd-f2ee3b564dab&r='+c+"%3A%2F%2Fads.servebom.com%2Fpartner%3Fcd%3D"+b+'%26svc%3Dus%26id%3D22%26uid%3D"></iframe>';userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create(9,"buyerzone.com|businessnewsdaily.com",false,function(){if(window.gdprUser)return;try{if(document.location.protocol==="http:"){var b=document.createElement("script");b.src="//sync.go.sonobi.com/uc.js";userSyncPixels._fragment.appendChild(b)}}catch(a){console.error(a)}try{var e=Math.floor(Math.random()*11E3),c=document.createElement("img"),d=document.location.protocol==="https:"?"https":"http";c.src=d+"://purch-sync.go.sonobi.com/us?"+d+"://ads.servebom.com/partner?cb="+
e+"&svc=us&id=9&uid=[UID]";userSyncPixels._fragment.appendChild(c)}catch(a){console.error(a)}});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create(24,"buyerzone.com|businessnewsdaily.com",false,function(){var a=document.createElement("iframe"),c=Math.floor(Math.random()*11E3);a.style.display="none";var b=document.location.protocol==="http:"?"http":"https";a.defer=true;a.src=b+"://ap.lijit.com/pixel?redir="+b+":%2F%2Fads.servebom.com%2Fpartner%3Fcb%3D"+c+"%26svc%3Dus%26id%3D24%26uid%3D$UID";userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create(14,"buyerzone.com|newegg.com|businessnewsdaily.com",false,function(){var a=document.createElement("span"),b=Math.floor(Math.random()*11E3);a.style.display="none";a.innerHTML='<iframe style="display:none" src="//eb2.3lift.com/getuid?redir=%2F%2Fads.servebom.com%2Fpartner%3Fcb%3D'+b+'%26svc%3Dus%26id%3D14%26uid%3D%24UID"></iframe>';userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create(5,"buyerzone.com|businessnewsdaily.com",false,function(){var a=document.createElement("span"),b=Math.floor(Math.random()*11E3);a.style.display="none";var c=document.location.protocol==="https:"?"https":"http";a.innerHTML='<iframe style="display:none" src="//ads.pubmatic.com/AdServer/js/user_sync.html?r='+b+"&p=46338&predirect="+c+"%3A%2F%2Fads.servebom.com%2Fpartner%3Fcd%3D"+b+'%26svc%3Dus%26id%3D5%26uid%3D"></iframe>';userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create(19,"buyerzone.com|businessnewsdaily.com",false,function(){var a=document.createElement("script");a.style.display="none";var c=document.location.protocol;a.defer=true;var b="assets.rubiconproject.com";if(document.location.protocol==="https:")b="secure-assets.rubiconproject.com";a.src=c+"//"+b+"/utils/xapi/multi-sync.js";a.dataset.partner="11868";a.dataset.region="na";a.dataset.country="us";a.dataset.endpoint="us-east";userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create(36,"buyerzone.com|businessnewsdaily.com",false,function(){var a=document.createElement("iframe"),c=Math.floor(Math.random()*11E3);a.style.display="none";var b=document.location.protocol==="http:"?"http":"https";a.defer=true;a.src=b+"://purch-match.dotomi.com/match/bounce/current?networkId=20077&version=1&rurl="+b+":%2F%2Fads.servebom.com%2Fpartner%3Fcb%3D"+c+"%26svc%3Dus%26id%3D36%26uid%3D$UID";userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create(45,"buyerzone.com|businessnewsdaily.com",false,function(){var a=document.createElement("span"),b=Math.floor(Math.random()*11E3);a.style.display="none";var c=document.location.protocol==="https:"?"https":"http";a.innerHTML='<iframe style="display:none" src="//ads.pubmatic.com/AdServer/js/user_sync.html?r='+b+"&p=46338&predirect="+c+"%3A%2F%2Fads.servebom.com%2Fpartner%3Fcd%3D"+b+'%26svc%3Dus%26id%3D45%26uid%3D"></iframe>';userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create(32,"space.com|tomsguide.com|tomshardware.com|livescience.com|laptopmag.com|newsarama.com|imore.com|androidcentral.com|windowscentral.com",true,function(){var c="ads.servebom.com",a=Math.floor(Math.random()*11E3),f="tmx_sync_"+a,b="qds0l";if(b===""||b.indexOf("$")===0)return;var d=document.createElement("span");d.style.display="none";var e=document.location.protocol==="http:"?"http":"https",b=b+".publishers.tremorhub.com",c=e+"://"+b+"/pubsync?redir="+e+":%2F%2F"+c+"%2Fpartner%3Fcb%3D"+a+"%26svc%3Dus%26id%3D32%26uid%3D%5Btvid%5D",a=document.createElement("iframe");
a.id=a.name=f;a.src=c;a.frameBorder=0;a.frameSpacing=0;a.scrolling="no";a.width=1;a.height=1;d.appendChild(a);userSyncPixels._fragment.appendChild(d)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create(17,"buyerzone.com|businessnewsdaily.com",false,function(){var b=document.location.protocol==="https:"?"https":"http",a=document.createElement("span"),c=Math.floor(Math.random()*11E3);a.style.display="none";a.innerHTML='<iframe style="display:none" src="'+b+"://bh.contextweb.com/bh/rtset?pid=558527&cb="+c+"&ev=1&rurl="+b+"%3A%2F%2Fads.servebom.com%2Fpartner%3Fsvc%3Dus%26id%3D17%26cb%3D"+c+'%26uid%3D%25%25VGUID%25%25"></iframe>';userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create(2,"buyerzone.com|businessnewsdaily.com",false,function(){var a=document.createElement("iframe"),b=Math.floor(Math.random()*11E3);a.style.display="none";var c=document.location.protocol;a.defer=true;var d="ssum.casalemedia.com";if(document.location.protocol==="https:")d="ssum-sec.casalemedia.com";a.src=c+"//"+d+"/usermatch?r="+b+"&s=181869&cb="+c+"%2F%2Fads.servebom.com%2Fpartner%3Fcb%3D"+b+"%26svc%3Dus%26id%3D2%26uid%3D";userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create(44,"buyerzone.com|businessnewsdaily.com",false,function(){var a=document.createElement("span"),b=Math.floor(Math.random()*11E3);a.style.display="none";var c=document.location.protocol==="https:"?"https":"http";a.innerHTML='<iframe style="display:none" src="//t.cwkuki.com/cs/prch18/?cb='+b+"&url="+c+"%3A%2F%2Fads.servebom.com%2Fpartner%3Fcb%3D"+b+'%26svc%3Dus%26id%3D44%26uid%3DD%5BUID%5D"></iframe>';userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

if(window.tmntag&&tmntag.isMobile&&!tmntag.isMobile())userSyncPixels.create(42,"buyerzone.com|businessnewsdaily.com",false,function(){var a=document.createElement("script");a.type="text/javascript";a.async=true;a.src="//sync.bfmio.com/syncb?pid=132";userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create(15,"buyerzone.com|businessnewsdaily.com",false,function(){var a=document.createElement("iframe"),c=Math.floor(Math.random()*11E3);a.style.display="none";var b=document.location.protocol;a.async=true;a.src=b+"//sync.adkernel.com/user-sync?zone=39660&r="+b+"%2F%2Fads.servebom.com%2Fpartner%3Fcb%3D"+c+"%26svc%3Dus%26id%3D15%26uid%3D{UID}";userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

userSyncPixels.create(46,"buyerzone.com|businessnewsdaily.com",false,function(){var a=document.createElement("span"),b=Math.floor(Math.random()*11E3);a.style.display="none";var c=document.location.protocol==="https:"?"https":"http";a.innerHTML='<iframe style="display:none" src="//ads.pubmatic.com/AdServer/js/user_sync.html?r='+b+"&p=156007&predirect="+c+"%3A%2F%2Fads.servebom.com%2Fpartner%3Fcd%3D"+b+'%26svc%3Dus%26id%3D46%26uid%3D"></iframe>';userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

var partnerId=27;userSyncPixels.create(partnerId,"buyerzone.com|businessnewsdaily.com",false,function(){var a=document.createElement("script");a.type="text/javascript";a.async=true;a.src="https://px.powerlinks.com/user/identify?rurl=https%3A%2F%2Fads.servebom.com%2Fpartner%3Fsvc%3Dus%26id%3D"+partnerId+"%26uid%3D${USER}";userSyncPixels._fragment.appendChild(a)});

});
} catch (e) {
console.error(e);
}
try {
tmntag_ready(function() {

(function(){document.body.appendChild(userSyncPixels._fragment)})();

});
} catch (e) {
console.error(e);
}
