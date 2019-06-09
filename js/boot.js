// !function() {
    // function e(e, n, t) {
    //     var o = new Image;
    //     o.onload = function(e) {
    //         "function" == typeof n && n.call(null, e)
    //     }
    //     ,
    //     o.onerror = function(e) {
    //         "function" == typeof t && t.call(null, e)
    //     }
    //     ,
    //     o.src = e
    // }
    // var n = window
    //   , t = n.document
    //   , o = require("disk-share:widget/data/yunData.js").get()
    //   , i = require("system-core:context/context.js")
    //   , r = i.instanceForSystem.libs.JQuery
    //   , a = i.instanceForSystem.libs.underscore
    //   , c = i.instanceForSystem.message
    //   , s = i.instanceForSystem.tools.baseService;
    // !function(e) {
    //     void 0 === e && (e = n.disk = {}),
    //     e.DEBUG = function() {
    //         var e = n.location.host;
    //         return n.console ? "pan.baidu.com" === e || "lab.pan.baidu.com" === e ? !1 : !0 : !1
    //     }(),
    //     e.uniqueId = 0,
    //     e.obtainId = function() {
    //         return "_disk_id_" + ++e.uniqueId
    //     }
    //     ,
    //     e.common = {}
    // }(n.disk);
    var u = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/~！@#￥%……&"
      , l = String.fromCharCode
      , d = function(e) {
        if (e.length < 2) {
            var n = e.charCodeAt(0);
            return 128 > n ? e : 2048 > n ? l(192 | n >>> 6) + l(128 | 63 & n) : l(224 | n >>> 12 & 15) + l(128 | n >>> 6 & 63) + l(128 | 63 & n)
        }
        var n = 65536 + 1024 * (e.charCodeAt(0) - 55296) + (e.charCodeAt(1) - 56320);
        return l(240 | n >>> 18 & 7) + l(128 | n >>> 12 & 63) + l(128 | n >>> 6 & 63) + l(128 | 63 & n)
    }
      , f = /[\uD800-\uDBFF][\uDC00-\uDFFFF]|[^\x00-\x7F]/g
      , g = function(e) {
        return (e + "" + Math.random()).replace(f, d)
    }
      , h = function(e) {
        var n = [0, 2, 1][e.length % 3]
          , t = e.charCodeAt(0) << 16 | (e.length > 1 ? e.charCodeAt(1) : 0) << 8 | (e.length > 2 ? e.charCodeAt(2) : 0)
          , o = [u.charAt(t >>> 18), u.charAt(t >>> 12 & 63), n >= 2 ? "=" : u.charAt(t >>> 6 & 63), n >= 1 ? "=" : u.charAt(63 & t)];
        return o.join("")
    }
      , m = function(e) {
        return e.replace(/[\s\S]{1,3}/g, h)
    }
      , p = function() {
        return m(g((new Date).getTime()))
    }
      , w = function(e, n) {
        return n ? p(String(e)).replace(/[+\/]/g, function(e) {
            return "+" == e ? "-" : "_"
        }).replace(/=/g, "") : p(String(e))
    };
    // !function() {
    function Getlogid(baiduid) {
        // r(document).ajaxSend(function(e, n, t) {
            // var i = w(s.getCookie("BAIDUID"));
            var i = w(baiduid);
            return i;
            // t.url += /\?/.test(t.url) ? "&channel=chunlei&web=1&app_id=250528" : "?channel=chunlei&web=1&app_id=250528",
            // ("script" !== t.dataType || t.cache !== !0) && (t.url += "&bdstoken=" + o.bdstoken + "&logid=" + i),
            // t.url += "/disk/plugin" === location.pathname ? "&clienttype=8&version=4.9.9.9" : "132" === s.getParam("msg") && s.getParam("devuid") ? "&clienttype=8" : "&clienttype=0"
        // })
    // }(),
    // }()
    }
    // function(e) {
    //     var n = e.async;
    //     e.async = function(e, t, o) {
    //         n(e, function() {
    //             "function" == typeof t && t.apply(this, arguments)
    //         }, function() {
    //             "function" == typeof o && o.apply(this, arguments)
    //         })
    //     }
    // }(require),
    // function() {
    //     r.browser.msie && 6 === parseInt(r.browser.version, 10) && t.execCommand("backgroundimagecache", !1, !0)
    // }(),
    // function(e) {
    //     e.trim || (e.trim = function() {
    //         return this.replace(/^\s+|\s+$/g, "")
    //     }
    //     )
    // }(String.prototype),
    // function(e) {
    //     e.indexOf || (e.indexOf = function(e) {
    //         return a.indexOf(this, e)
    //     }
    //     ,
    //     e.forEach || (e.forEach = function(e) {
    //         return a.each(this, e)
    //     }
    //     ))
    // }(Array.prototype),
    // function() {
    //     r.browser.msie === !0 && 6 == r.browser.version && r("body").addClass("fixbug-ie6")
    // }(),
    // function() {
    //     c.once("after-list-loaded", function() {
    //         require.async("disk-share:static/js/pcsDownloadUtil.js", function(e) {
    //             e.initPcsDownloadCdnConnectivity(function(e) {
    //                 e && i.instanceForSystem.file.watchCDNOfPCS(e)
    //             })
    //         })
    //     })
    // }(),
    // function() {
    //     Object.defineProperty && (Object.defineProperty(window, "navigator", {
    //         configurable: !1,
    //         writable: !1,
    //         value: window.navigator
    //     }),
    //     Object.defineProperty(window.navigator, "platform", {
    //         configurable: !1,
    //         writable: !1,
    //         value: window.navigator.platform
    //     }),
    //     Object.defineProperty(window.navigator, "userAgent", {
    //         configurable: !1,
    //         writable: !1,
    //         value: window.navigator.userAgent
    //     }))
    // }(),
    // window.location.origin || (window.location.origin = window.location.protocol + "//" + window.location.hostname + (window.location.port ? ":" + window.location.port : "")),
    // function() {
    //     for (var e = ["Hm_lvt_773fea2ac036979ebb5fcc768d8beb67", "Hm_lvt_b181fb73f90936ebd334d457c848c8b5", "Hm_lvt_adf736c22cd6bcc36a1d27e5af30949e"], n = "." + location.hostname, t = 0; t < e.length; t++)
    //         s.setCookie(e[t], "", -1, "/", n)
    // }();
    // var v = s.client();
    // if ("/disk/home" === location.pathname) {
    //     var b = null
    //       , y = v.browserString
    //       , S = 30
    //       , k = 0
    //       , x = 2e3;
    //     (-1 !== y.indexOf("chrome") || -1 !== y.indexOf("firefox") || -1 !== y.indexOf("safari")) && (b = setInterval(function() {
    //         var e = r("script")
    //           , n = e[e.length - 1].src;
    //         (-1 !== n.indexOf("mjaenbjdjmgolhoafkohbhhbaiedbkno") || -1 !== n.indexOf("acgotaku311") || -1 !== n.indexOf("BaiduExporter")) && (i.instanceForSystem.log.send({
    //             name: "chrome-extension",
    //             sendServerLog: !0,
    //             value: y
    //         }),
    //         clearInterval(b)),
    //         ++k > S && clearInterval(b)
    //     }, x),
    //     r(document).delegate("#export_menu", "click", function() {
    //         i.instanceForSystem.log.send({
    //             name: "chrome-used",
    //             sendServerLog: !0,
    //             value: y
    //         })
    //     }))
    // }
    // "http:" !== location.protocol || !v.engine || null == v.engine.ie || "ie11" !== v.browserString && "edge" !== v.browserString || e("https://" + location.host + "/yun-static/common/images/default.gif", function() {
    //     s.setCookie("secu", 1, 365, "/"),
    //     i.instanceForSystem.log.send({
    //         type: "httpsAccess" + v.browserString
    //     })
    // }),
    // "https:" === location.protocol && "serviceWorker"in navigator && navigator.userAgent.indexOf("Firefox") <= -1 && navigator.serviceWorker.register("/disk/serviceworker.js", {
    //     scope: "/disk/home"
    // }).then(function(e) {
    //     e.installing ? console.log("Service worker installing") : e.waiting ? console.log("Service worker installed") : e.active && console.log("Service worker active")
    // }, function(e) {
    //     console.log(e)
    // });
    // var C = function() {
    //     var e = document.referrer;
    //     if ("string" == typeof e && e.length > 0) {
    //         var n = "fm_self"
    //           , t = /(http|https):\/\/(tieba|hao123)\.baidu\.com/gi
    //           , o = /(http|https):\/\/www\.hao123\.com/gi;
    //         t.test(e) ? n = "fm_" + RegExp.$2 : o.test(e) ? n = "fm_hao123" : -1 !== e.indexOf("http://www.baidu.com/s?wd=") && (n = "fm_baidups")
    //     }
    //     return n
    // }();
    // i.instanceForSystem.log.sendUserReport(C)
// }();
