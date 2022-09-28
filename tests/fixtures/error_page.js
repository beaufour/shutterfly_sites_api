window.Shr = window.Shr || {};
Shr.AS = {
  domain: "shutterfly.com",
  site: "site.shutterfly.com",
  cmd: "cmd.shutterfly.com",
  cmd2: "cmd2.shutterfly.com",
  staticServer: "cdn.staticsfly.com",
  staticServer2: "web1.shutterfly.com",
  staticVersionFiles: true,
  env: null,
  www: "www.shutterfly.com",
  web: "web.shutterfly.com",
  imgsize: 0,
  community: "community.shutterfly.com",
  img: "uniim-share.shutterfly.com",
  c1: "c1.staticsfly.com",
  gim: "gim.shutterfly.com",
  up: "up1.shutterfly.com",
  uniup: "uniup.shutterfly.com",
  ws: "ws-internal.internal.shutterfly.com",
  api: "api.shutterfly.com",
  audio: "soundnode.shutterfly.com/audio/encode",
  mname: "ip-0A9301DF",
  mailDomain: "sfly.com",
  hasVersionedPaths: true,
  sca: "sflyprod",
  video: "sfly",
  videoStreamBaseUrl: "s2l7lz1oe5m0jf.cloudfront.net",
  mixStreamBaseUrl: "s3s7goqqfk1hjc.cloudfront.net",
  videoHttpBaseUrl: "d23sq69wqfvv5f.cloudfront.net",
  mixHttpBaseUrl: "d27hg30z5i8vu1.cloudfront.net",
  version: "2.0.8291.7803",
  versionDate: "9/13/2022 4:20:06 AM",
};
Shr.AD = {
  start: 1664323498,
  siteMessage: "",
  EnableAcceptanceFlow: true,
  Features: {
    SplunkLoggingEnabled: true,
    WebSplunkLoggingEnabled: true,
    WebOptimizelyEnabled: true,
    WebBulkContactsImportEnabled: false,
    WebNewEmailInvitesEnabled: true,
  },
};
Shr.AR = {
  h2: "LUGfUP-wPSfXhN8nqYtdVnc1-cC_v8jPPb0PF4EJVs5kxt_OKjtBAFh6fxw-JcB3hy1UPxYkTu8aOBbKfEmoa067vSA1",
};
Shr.US = {};
Shr.U = {
  visitorId: "70fedac6-9ea4-47cd-bee7-e8480ca46485",
  dateFormat: "m",
  timeFormat: "1",
  temperatureUnits: "f",
};
Shr.UP = {};
Shr.UB = { name: "gecko", platform: "Unknown", major: 96 };
Shr.S = {
  noStore: true,
  siteName: "dwightexplorers4",
  role: -2,
  collectionKey: "kActmTRqzaN2TJ2g",
  albumKey: "67b0de21b3d0d21125ae",
  createdBy: "022074354269",
  displayName: "Explorers4",
  displayName2: "Explorers4",
  template: "g_classroom_t2",
  category: "classroom",
  noShareOut: -4,
  noShareEmail: -1,
  sitePermission: "Members",
  pages: [],
  membershipType: 1,
  hideMembers: true,
  ageGroup: "99",
  schoolName: "Dwight Preschool",
  schoolCity: "New York",
  schoolState: "NY",
  subcategory: "teacher",
  timeZone: "(GMT-05:00) Eastern Time",
};
Shr.ADV = {
  domainPrefix: "dwightexplorers4.shutterfly.com",
  creatorUID: "022074354269",
  customAdParams: "/template=classroom.teacher.99",
  customAdParams2: "classroom.teacher.99",
  src: "//iframe.shutterfly.com/servlet/AdServlet",
};
Shr.P = {
  pageId: "dwightexplorers4/pictures",
  version: 0,
  changeId: 0,
  kind: "ErrorPage",
  title: "Private site",
  layout: "w",
  pageLayout: "Security",
  role: -2,
  up: 0,
  vp: 0,
  readers: "Members",
  sections: [
    {
      zid: "1",
      mid: "PrivatePage",
      bid: "b",
      lid: "sfly",
      contentId: "ErrorNoUser",
      nodeId: 2,
      isCookied: false,
      email: "",
      isSiteMember: false,
      contentId: "ErrorNoUser",
      isUser: false,
    },
  ],
  createdBy: "022074354269",
};
Shr.PM = {
  js1: ["//cdn.staticsfly.com/shr/c/common/combined/1454775e.js"],
  js2: [],
  js3: [
    "//cdn.staticsfly.com/shr/c/dialog2/f7b8d228.js",
    "//cdn.staticsfly.com/shr/c/dialogs/password/7ed0b522.js",
    "//cdn.staticsfly.com/shr/t/navyblue/theme/fb5626f7.js",
  ],
  js4: ["//cdn.staticsfly.com/shr/m/privatepage/privatepage/b18163a3.js"],
  js5: [],
  styles: [
    "//cdn.staticsfly.com/shr/t/base/theme/0b21c2c6.css",
    "//cdn.staticsfly.com/shr/t/navyblue/theme/c722198a.css",
  ],
};
Shr.PD = [];
Shr.SD = {
  site: {
    rosterItemName: "Child",
    rosterItemsName: "Children",
    rosterItemNameLower: "child",
    rosterItemsNameLower: "children",
  },
};
Shr.AL = {
  js: function (a) {
    var ctx = Shr.context || {};
    if (ctx.renderJavaScript) {
      ctx.renderJavaScript(a);
    } else if (a) {
      var i = 0,
        l = a.length;
      for (; i < l; i++) {
        document.write(
          '<script type="text/javascript" src="' + a[i] + '"></script>'
        );
      }
    }
  },
  css: function (a) {
    var ctx = Shr.context || {};
    if (ctx.renderStyleSheets) {
      ctx.renderStyleSheets(a);
    } else if (a) {
      var i = 0,
        l = a.length;
      for (; i < l; i++) {
        document.write(
          '<link rel="stylesheet" type="text/css" id="' +
          a[i] +
          '"  href="' +
          a[i] +
          '" />'
        );
      }
    }
  },
};
Shr.AL.js(Shr.PM.js1);
Shr.AL.js(Shr.PM.js2);
Shr.AL.js(Shr.PM.js3);
Shr.AL.js(Shr.PM.js4);
Shr.AL.js(Shr.PM.js5);
Shr.AL.css(Shr.PM.styles);
