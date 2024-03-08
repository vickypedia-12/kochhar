from scrapy import Selector

# HTML string
html_string = """
<!DOCTYPE html>
<!--[if IE 6]>
<html id="ie6" lang="en-US">
<![endif]-->
<!--[if IE 7]>
<html id="ie7" lang="en-US">
<![endif]-->
<!--[if IE 8]>
<html id="ie8" lang="en-US">
<![endif]-->
<!--[if !(IE 6) | !(IE 7) | !(IE 8)  ]><!-->
<html lang="en-US">
<!--<![endif]-->

<head>
	<meta charset="UTF-8" />
	<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
	<meta http-equiv="Pragma" content="no-cache">
	<meta http-equiv="Expires" content="0">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	<title>
		Updates &amp; Insights |Kochhar &amp; Co </title>
	<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />

	<!-- This site is optimized with the Yoast SEO plugin v18.0 - https://yoast.com/wordpress/plugins/seo/ -->
	<meta name="description"
		content="Knowledge repository of Legal Alerts &amp; Updates, Publications, Insights, Webcasts &amp; Podcasts" />
	<link rel="canonical" href="https://kochhar.com/knowledge-centre/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="Updates &amp; Insights |" />
	<meta property="og:description"
		content="Knowledge repository of Legal Alerts &amp; Updates, Publications, Insights, Webcasts &amp; Podcasts" />
	<meta property="og:url" content="https://kochhar.com/knowledge-centre/" />
	<meta property="og:site_name" content="Kochhar &amp; Co" />
	<meta property="article:publisher" content="https://www.facebook.com/Kochharandcompany" />
	<meta property="article:modified_time" content="2022-02-21T11:38:33+00:00" />
	<meta property="og:image" content="https://kochhar.com/wp-content/uploads/2021/09/Knowledge-Centre.png" />
	<meta property="og:image:width" content="1380" />
	<meta property="og:image:height" content="180" />
	<meta property="og:image:type" content="image/png" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:site" content="@KochharAndCo" />
	<script type="application/ld+json" class="yoast-schema-graph">
		{"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":"https://kochhar.com/#website","url":"https://kochhar.com/","name":"Kochhar &amp; Co","description":"Advocates and Legal Consultants","potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://kochhar.com/?s={search_term_string}"},"query-input":"required name=search_term_string"}],"inLanguage":"en-US"},{"@type":"ImageObject","@id":"https://kochhar.com/knowledge-centre/#primaryimage","inLanguage":"en-US","url":"https://kochhar.com/wp-content/uploads/2021/09/Knowledge-Centre.png","contentUrl":"https://kochhar.com/wp-content/uploads/2021/09/Knowledge-Centre.png","width":1380,"height":180},{"@type":"WebPage","@id":"https://kochhar.com/knowledge-centre/#webpage","url":"https://kochhar.com/knowledge-centre/","name":"Updates & Insights |","isPartOf":{"@id":"https://kochhar.com/#website"},"primaryImageOfPage":{"@id":"https://kochhar.com/knowledge-centre/#primaryimage"},"datePublished":"2021-04-30T06:12:22+00:00","dateModified":"2022-02-21T11:38:33+00:00","description":"Knowledge repository of Legal Alerts & Updates, Publications, Insights, Webcasts & Podcasts","breadcrumb":{"@id":"https://kochhar.com/knowledge-centre/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https://kochhar.com/knowledge-centre/"]}]},{"@type":"BreadcrumbList","@id":"https://kochhar.com/knowledge-centre/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://kochhar.com/"},{"@type":"ListItem","position":2,"name":"knowledge centre"}]}]}
	</script>
	<!-- / Yoast SEO plugin. -->


	<link rel='dns-prefetch' href='//cdn.jsdelivr.net' />
	<link rel='dns-prefetch' href='//fonts.googleapis.com' />
	<script type="text/javascript">
		/* <![CDATA[ */
window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/14.0.0\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/14.0.0\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/kochhar.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=6.4.3"}};
/*! This file is auto-generated */
!function(i,n){var o,s,e;function c(e){try{var t={supportTests:e,timestamp:(new Date).valueOf()};sessionStorage.setItem(o,JSON.stringify(t))}catch(e){}}function p(e,t,n){e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(t,0,0);var t=new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data),r=(e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(n,0,0),new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data));return t.every(function(e,t){return e===r[t]})}function u(e,t,n){switch(t){case"flag":return n(e,"\ud83c\udff3\ufe0f\u200d\u26a7\ufe0f","\ud83c\udff3\ufe0f\u200b\u26a7\ufe0f")?!1:!n(e,"\ud83c\uddfa\ud83c\uddf3","\ud83c\uddfa\u200b\ud83c\uddf3")&&!n(e,"\ud83c\udff4\udb40\udc67\udb40\udc62\udb40\udc65\udb40\udc6e\udb40\udc67\udb40\udc7f","\ud83c\udff4\u200b\udb40\udc67\u200b\udb40\udc62\u200b\udb40\udc65\u200b\udb40\udc6e\u200b\udb40\udc67\u200b\udb40\udc7f");case"emoji":return!n(e,"\ud83e\udef1\ud83c\udffb\u200d\ud83e\udef2\ud83c\udfff","\ud83e\udef1\ud83c\udffb\u200b\ud83e\udef2\ud83c\udfff")}return!1}function f(e,t,n){var r="undefined"!=typeof WorkerGlobalScope&&self instanceof WorkerGlobalScope?new OffscreenCanvas(300,150):i.createElement("canvas"),a=r.getContext("2d",{willReadFrequently:!0}),o=(a.textBaseline="top",a.font="600 32px Arial",{});return e.forEach(function(e){o[e]=t(a,e,n)}),o}function t(e){var t=i.createElement("script");t.src=e,t.defer=!0,i.head.appendChild(t)}"undefined"!=typeof Promise&&(o="wpEmojiSettingsSupports",s=["flag","emoji"],n.supports={everything:!0,everythingExceptFlag:!0},e=new Promise(function(e){i.addEventListener("DOMContentLoaded",e,{once:!0})}),new Promise(function(t){var n=function(){try{var e=JSON.parse(sessionStorage.getItem(o));if("object"==typeof e&&"number"==typeof e.timestamp&&(new Date).valueOf()<e.timestamp+604800&&"object"==typeof e.supportTests)return e.supportTests}catch(e){}return null}();if(!n){if("undefined"!=typeof Worker&&"undefined"!=typeof OffscreenCanvas&&"undefined"!=typeof URL&&URL.createObjectURL&&"undefined"!=typeof Blob)try{var e="postMessage("+f.toString()+"("+[JSON.stringify(s),u.toString(),p.toString()].join(",")+"));",r=new Blob([e],{type:"text/javascript"}),a=new Worker(URL.createObjectURL(r),{name:"wpTestEmojiSupports"});return void(a.onmessage=function(e){c(n=e.data),a.terminate(),t(n)})}catch(e){}c(n=f(s,u,p))}t(n)}).then(function(e){for(var t in e)n.supports[t]=e[t],n.supports.everything=n.supports.everything&&n.supports[t],"flag"!==t&&(n.supports.everythingExceptFlag=n.supports.everythingExceptFlag&&n.supports[t]);n.supports.everythingExceptFlag=n.supports.everythingExceptFlag&&!n.supports.flag,n.DOMReady=!1,n.readyCallback=function(){n.DOMReady=!0}}).then(function(){return e}).then(function(){var e;n.supports.everything||(n.readyCallback(),(e=n.source||{}).concatemoji?t(e.concatemoji):e.wpemoji&&e.twemoji&&(t(e.twemoji),t(e.wpemoji)))}))}((window,document),window._wpemojiSettings);
/* ]]> */
	</script>
	<style id='wp-emoji-styles-inline-css' type='text/css'>
		img.wp-smiley,
		img.emoji {
			display: inline !important;
			border: none !important;
			box-shadow: none !important;
			height: 1em !important;
			width: 1em !important;
			margin: 0 0.07em !important;
			vertical-align: -0.1em !important;
			background: none !important;
			padding: 0 !important;
		}
	</style>
	<link rel='stylesheet' id='wp-block-library-css'
		href='https://kochhar.com/wp-includes/css/dist/block-library/style.min.css?ver=6.4.3' type='text/css'
		media='all' />
	<style id='classic-theme-styles-inline-css' type='text/css'>
		/*! This file is auto-generated */
		.wp-block-button__link {
			color: #fff;
			background-color: #32373c;
			border-radius: 9999px;
			box-shadow: none;
			text-decoration: none;
			padding: calc(.667em + 2px) calc(1.333em + 2px);
			font-size: 1.125em
		}

		.wp-block-file__button {
			background: #32373c;
			color: #fff;
			text-decoration: none
		}
	</style>
	<style id='global-styles-inline-css' type='text/css'>
		body {
			--wp--preset--color--black: #000000;
			--wp--preset--color--cyan-bluish-gray: #abb8c3;
			--wp--preset--color--white: #ffffff;
			--wp--preset--color--pale-pink: #f78da7;
			--wp--preset--color--vivid-red: #cf2e2e;
			--wp--preset--color--luminous-vivid-orange: #ff6900;
			--wp--preset--color--luminous-vivid-amber: #fcb900;
			--wp--preset--color--light-green-cyan: #7bdcb5;
			--wp--preset--color--vivid-green-cyan: #00d084;
			--wp--preset--color--pale-cyan-blue: #8ed1fc;
			--wp--preset--color--vivid-cyan-blue: #0693e3;
			--wp--preset--color--vivid-purple: #9b51e0;
			--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg, rgba(6, 147, 227, 1) 0%, rgb(155, 81, 224) 100%);
			--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg, rgb(122, 220, 180) 0%, rgb(0, 208, 130) 100%);
			--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg, rgba(252, 185, 0, 1) 0%, rgba(255, 105, 0, 1) 100%);
			--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg, rgba(255, 105, 0, 1) 0%, rgb(207, 46, 46) 100%);
			--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg, rgb(238, 238, 238) 0%, rgb(169, 184, 195) 100%);
			--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg, rgb(74, 234, 220) 0%, rgb(151, 120, 209) 20%, rgb(207, 42, 186) 40%, rgb(238, 44, 130) 60%, rgb(251, 105, 98) 80%, rgb(254, 248, 76) 100%);
			--wp--preset--gradient--blush-light-purple: linear-gradient(135deg, rgb(255, 206, 236) 0%, rgb(152, 150, 240) 100%);
			--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg, rgb(254, 205, 165) 0%, rgb(254, 45, 45) 50%, rgb(107, 0, 62) 100%);
			--wp--preset--gradient--luminous-dusk: linear-gradient(135deg, rgb(255, 203, 112) 0%, rgb(199, 81, 192) 50%, rgb(65, 88, 208) 100%);
			--wp--preset--gradient--pale-ocean: linear-gradient(135deg, rgb(255, 245, 203) 0%, rgb(182, 227, 212) 50%, rgb(51, 167, 181) 100%);
			--wp--preset--gradient--electric-grass: linear-gradient(135deg, rgb(202, 248, 128) 0%, rgb(113, 206, 126) 100%);
			--wp--preset--gradient--midnight: linear-gradient(135deg, rgb(2, 3, 129) 0%, rgb(40, 116, 252) 100%);
			--wp--preset--font-size--small: 13px;
			--wp--preset--font-size--medium: 20px;
			--wp--preset--font-size--large: 36px;
			--wp--preset--font-size--x-large: 42px;
			--wp--preset--spacing--20: 0.44rem;
			--wp--preset--spacing--30: 0.67rem;
			--wp--preset--spacing--40: 1rem;
			--wp--preset--spacing--50: 1.5rem;
			--wp--preset--spacing--60: 2.25rem;
			--wp--preset--spacing--70: 3.38rem;
			--wp--preset--spacing--80: 5.06rem;
			--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);
			--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);
			--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);
			--wp--preset--shadow--outlined: 6px 6px 0px -3px rgba(255, 255, 255, 1), 6px 6px rgba(0, 0, 0, 1);
			--wp--preset--shadow--crisp: 6px 6px 0px rgba(0, 0, 0, 1);
		}

		:where(.is-layout-flex) {
			gap: 0.5em;
		}

		:where(.is-layout-grid) {
			gap: 0.5em;
		}

		body .is-layout-flow>.alignleft {
			float: left;
			margin-inline-start: 0;
			margin-inline-end: 2em;
		}

		body .is-layout-flow>.alignright {
			float: right;
			margin-inline-start: 2em;
			margin-inline-end: 0;
		}

		body .is-layout-flow>.aligncenter {
			margin-left: auto !important;
			margin-right: auto !important;
		}

		body .is-layout-constrained>.alignleft {
			float: left;
			margin-inline-start: 0;
			margin-inline-end: 2em;
		}

		body .is-layout-constrained>.alignright {
			float: right;
			margin-inline-start: 2em;
			margin-inline-end: 0;
		}

		body .is-layout-constrained>.aligncenter {
			margin-left: auto !important;
			margin-right: auto !important;
		}

		body .is-layout-constrained> :where(:not(.alignleft):not(.alignright):not(.alignfull)) {
			max-width: var(--wp--style--global--content-size);
			margin-left: auto !important;
			margin-right: auto !important;
		}

		body .is-layout-constrained>.alignwide {
			max-width: var(--wp--style--global--wide-size);
		}

		body .is-layout-flex {
			display: flex;
		}

		body .is-layout-flex {
			flex-wrap: wrap;
			align-items: center;
		}

		body .is-layout-flex>* {
			margin: 0;
		}

		body .is-layout-grid {
			display: grid;
		}

		body .is-layout-grid>* {
			margin: 0;
		}

		:where(.wp-block-columns.is-layout-flex) {
			gap: 2em;
		}

		:where(.wp-block-columns.is-layout-grid) {
			gap: 2em;
		}

		:where(.wp-block-post-template.is-layout-flex) {
			gap: 1.25em;
		}

		:where(.wp-block-post-template.is-layout-grid) {
			gap: 1.25em;
		}

		.has-black-color {
			color: var(--wp--preset--color--black) !important;
		}

		.has-cyan-bluish-gray-color {
			color: var(--wp--preset--color--cyan-bluish-gray) !important;
		}

		.has-white-color {
			color: var(--wp--preset--color--white) !important;
		}

		.has-pale-pink-color {
			color: var(--wp--preset--color--pale-pink) !important;
		}

		.has-vivid-red-color {
			color: var(--wp--preset--color--vivid-red) !important;
		}

		.has-luminous-vivid-orange-color {
			color: var(--wp--preset--color--luminous-vivid-orange) !important;
		}

		.has-luminous-vivid-amber-color {
			color: var(--wp--preset--color--luminous-vivid-amber) !important;
		}

		.has-light-green-cyan-color {
			color: var(--wp--preset--color--light-green-cyan) !important;
		}

		.has-vivid-green-cyan-color {
			color: var(--wp--preset--color--vivid-green-cyan) !important;
		}

		.has-pale-cyan-blue-color {
			color: var(--wp--preset--color--pale-cyan-blue) !important;
		}

		.has-vivid-cyan-blue-color {
			color: var(--wp--preset--color--vivid-cyan-blue) !important;
		}

		.has-vivid-purple-color {
			color: var(--wp--preset--color--vivid-purple) !important;
		}

		.has-black-background-color {
			background-color: var(--wp--preset--color--black) !important;
		}

		.has-cyan-bluish-gray-background-color {
			background-color: var(--wp--preset--color--cyan-bluish-gray) !important;
		}

		.has-white-background-color {
			background-color: var(--wp--preset--color--white) !important;
		}

		.has-pale-pink-background-color {
			background-color: var(--wp--preset--color--pale-pink) !important;
		}

		.has-vivid-red-background-color {
			background-color: var(--wp--preset--color--vivid-red) !important;
		}

		.has-luminous-vivid-orange-background-color {
			background-color: var(--wp--preset--color--luminous-vivid-orange) !important;
		}

		.has-luminous-vivid-amber-background-color {
			background-color: var(--wp--preset--color--luminous-vivid-amber) !important;
		}

		.has-light-green-cyan-background-color {
			background-color: var(--wp--preset--color--light-green-cyan) !important;
		}

		.has-vivid-green-cyan-background-color {
			background-color: var(--wp--preset--color--vivid-green-cyan) !important;
		}

		.has-pale-cyan-blue-background-color {
			background-color: var(--wp--preset--color--pale-cyan-blue) !important;
		}

		.has-vivid-cyan-blue-background-color {
			background-color: var(--wp--preset--color--vivid-cyan-blue) !important;
		}

		.has-vivid-purple-background-color {
			background-color: var(--wp--preset--color--vivid-purple) !important;
		}

		.has-black-border-color {
			border-color: var(--wp--preset--color--black) !important;
		}

		.has-cyan-bluish-gray-border-color {
			border-color: var(--wp--preset--color--cyan-bluish-gray) !important;
		}

		.has-white-border-color {
			border-color: var(--wp--preset--color--white) !important;
		}

		.has-pale-pink-border-color {
			border-color: var(--wp--preset--color--pale-pink) !important;
		}

		.has-vivid-red-border-color {
			border-color: var(--wp--preset--color--vivid-red) !important;
		}

		.has-luminous-vivid-orange-border-color {
			border-color: var(--wp--preset--color--luminous-vivid-orange) !important;
		}

		.has-luminous-vivid-amber-border-color {
			border-color: var(--wp--preset--color--luminous-vivid-amber) !important;
		}

		.has-light-green-cyan-border-color {
			border-color: var(--wp--preset--color--light-green-cyan) !important;
		}

		.has-vivid-green-cyan-border-color {
			border-color: var(--wp--preset--color--vivid-green-cyan) !important;
		}

		.has-pale-cyan-blue-border-color {
			border-color: var(--wp--preset--color--pale-cyan-blue) !important;
		}

		.has-vivid-cyan-blue-border-color {
			border-color: var(--wp--preset--color--vivid-cyan-blue) !important;
		}

		.has-vivid-purple-border-color {
			border-color: var(--wp--preset--color--vivid-purple) !important;
		}

		.has-vivid-cyan-blue-to-vivid-purple-gradient-background {
			background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;
		}

		.has-light-green-cyan-to-vivid-green-cyan-gradient-background {
			background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;
		}

		.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background {
			background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;
		}

		.has-luminous-vivid-orange-to-vivid-red-gradient-background {
			background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;
		}

		.has-very-light-gray-to-cyan-bluish-gray-gradient-background {
			background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;
		}

		.has-cool-to-warm-spectrum-gradient-background {
			background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;
		}

		.has-blush-light-purple-gradient-background {
			background: var(--wp--preset--gradient--blush-light-purple) !important;
		}

		.has-blush-bordeaux-gradient-background {
			background: var(--wp--preset--gradient--blush-bordeaux) !important;
		}

		.has-luminous-dusk-gradient-background {
			background: var(--wp--preset--gradient--luminous-dusk) !important;
		}

		.has-pale-ocean-gradient-background {
			background: var(--wp--preset--gradient--pale-ocean) !important;
		}

		.has-electric-grass-gradient-background {
			background: var(--wp--preset--gradient--electric-grass) !important;
		}

		.has-midnight-gradient-background {
			background: var(--wp--preset--gradient--midnight) !important;
		}

		.has-small-font-size {
			font-size: var(--wp--preset--font-size--small) !important;
		}

		.has-medium-font-size {
			font-size: var(--wp--preset--font-size--medium) !important;
		}

		.has-large-font-size {
			font-size: var(--wp--preset--font-size--large) !important;
		}

		.has-x-large-font-size {
			font-size: var(--wp--preset--font-size--x-large) !important;
		}

		.wp-block-navigation a:where(:not(.wp-element-button)) {
			color: inherit;
		}

		:where(.wp-block-post-template.is-layout-flex) {
			gap: 1.25em;
		}

		:where(.wp-block-post-template.is-layout-grid) {
			gap: 1.25em;
		}

		:where(.wp-block-columns.is-layout-flex) {
			gap: 2em;
		}

		:where(.wp-block-columns.is-layout-grid) {
			gap: 2em;
		}

		.wp-block-pullquote {
			font-size: 1.5em;
			line-height: 1.6;
		}
	</style>
	<link rel='stylesheet' id='contact-form-7-css'
		href='https://kochhar.com/wp-content/plugins/contact-form-7/includes/css/styles.css?ver=5.5.6.1' type='text/css'
		media='all' />
	<link rel='stylesheet' id='email-subscribers-css'
		href='https://kochhar.com/wp-content/plugins/email-subscribers/lite/public/css/email-subscribers-public.css?ver=5.3.15'
		type='text/css' media='all' />
	<link rel='stylesheet' id='sfwppa-public-style-css'
		href='https://kochhar.com/wp-content/plugins/styles-for-wp-pagenavi-addon/assets/css/sfwppa-style.css?ver=1.2.1'
		type='text/css' media='all' />
	<link rel='stylesheet' id='wp-job-manager-job-listings-css'
		href='https://kochhar.com/wp-content/plugins/wp-job-manager/assets/dist/css/job-listings.css?ver=598383a28ac5f9f156e4'
		type='text/css' media='all' />
	<link rel='stylesheet' id='wp-pagenavi-css'
		href='https://kochhar.com/wp-content/plugins/wp-pagenavi/pagenavi-css.css?ver=2.70' type='text/css'
		media='all' />
	<link rel='stylesheet' id='megamenu-css'
		href='https://kochhar.com/wp-content/uploads/maxmegamenu/style.css?ver=9bd6cd' type='text/css' media='all' />
	<link rel='stylesheet' id='dashicons-css' href='https://kochhar.com/wp-includes/css/dashicons.min.css?ver=6.4.3'
		type='text/css' media='all' />
	<link rel='stylesheet' id='bootstrap_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/bootstrap.min.css?ver=6.4.3'
		type='text/css' media='all' />
	<link rel='stylesheet' id='custom-google-fonts-css'
		href='https://fonts.googleapis.com/css2?family=Josefin+Sans%3Awght%40300%3B400%3B500%3B600&#038;display=swap&#038;ver=6.4.3'
		type='text/css' media='all' />
	<link rel='stylesheet' id='font-awesome-css'
		href='https://kochhar.com/wp-content/plugins/elementor/assets/lib/font-awesome/css/font-awesome.min.css?ver=4.7.0'
		type='text/css' media='all' />
	<link rel='stylesheet' id='fancybox_css-css'
		href='https://cdn.jsdelivr.net/npm/@fancyapps/ui/dist/fancybox.css?ver=6.4.3' type='text/css' media='all' />
	<link rel='stylesheet' id='slicknav_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/slicknav.css?ver=6.4.3' type='text/css'
		media='all' />
	<link rel='stylesheet' id='jquery_bxslider_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/jquery.bxslider.css?ver=6.4.3'
		type='text/css' media='all' />
	<link rel='stylesheet' id='owl_carousel_min_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/owl.carousel.min.css?ver=6.4.3'
		type='text/css' media='all' />
	<link rel='stylesheet' id='owl_theme_default_min_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/owl.theme.default.min.css?ver=6.4.3'
		type='text/css' media='all' />
	<link rel='stylesheet' id='easy_responsive_tabs-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/easy-responsive-tabs.css?ver=6.4.3'
		type='text/css' media='all' />
	<link rel='stylesheet' id='bootstrap_select_min_css-css'
		href='//cdn.jsdelivr.net/npm/bootstrap-select@1.14.0-beta2/dist/css/bootstrap-select.min.css?ver=6.4.3'
		type='text/css' media='all' />
	<link rel='stylesheet' id='main_css-css' href='https://kochhar.com/wp-content/themes/kochhar-theme/style.css?ver=22'
		type='text/css' media='all' />
	<link rel='stylesheet' id='styleMax320_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/styleMax320.css?ver=96' type='text/css'
		media='only screen and (max-width: 320px)' />
	<link rel='stylesheet' id='styleMax480_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/styleMax480.css?ver=16' type='text/css'
		media='only screen and (min-width: 321px) and (max-width: 480px)' />
	<link rel='stylesheet' id='styleMax768_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/styleMax768.css?ver=35' type='text/css'
		media='only screen and (min-width: 481px) and (max-width: 768px)' />
	<link rel='stylesheet' id='styleMax992_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/styleMax992.css?ver=32' type='text/css'
		media='only screen and (min-width: 769px) and (max-width: 992px)' />
	<link rel='stylesheet' id='styleMax1024_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/styleMax1024.css?ver=26' type='text/css'
		media='only screen and (min-width: 993px) and (max-width: 1025px)' />
	<link rel='stylesheet' id='styleMax1280_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/styleMax1280.css?ver=61' type='text/css'
		media='only screen and (min-width: 1026px) and (max-width: 1290px)' />
	<link rel='stylesheet' id='styleMax1440_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/styleMax1440.css?ver=46' type='text/css'
		media='only screen and (min-width: 1291px) and (max-width: 1450px)' />
	<link rel='stylesheet' id='styleMax1600_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/styleMax1600.css?ver=91' type='text/css'
		media='only screen and (min-width: 1451px) and (max-width: 1620px)' />
	<link rel='stylesheet' id='styleMax1680_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/styleMax1680.css?ver=84' type='text/css'
		media='only screen and (min-width: 1621px) and (max-width: 1690px)' />
	<link rel='stylesheet' id='styleMax1920_css-css'
		href='https://kochhar.com/wp-content/themes/kochhar-theme/assets/css/styleMax1920.css?ver=78' type='text/css'
		media='only screen and (min-width: 1691px) and (max-width: 1920px)' />
	<link rel='stylesheet' id='elementor-icons-ekiticons-css'
		href='https://kochhar.com/wp-content/plugins/elementskit-lite/modules/elementskit-icon-pack/assets/css/ekiticons.css?ver=3.0.2'
		type='text/css' media='all' />
	<link rel='stylesheet' id='elementor-icons-css'
		href='https://kochhar.com/wp-content/plugins/elementor/assets/lib/eicons/css/elementor-icons.min.css?ver=5.11.0'
		type='text/css' media='all' />
	<link rel='stylesheet' id='elementor-animations-css'
		href='https://kochhar.com/wp-content/plugins/elementor/assets/lib/animations/animations.min.css?ver=3.1.4'
		type='text/css' media='all' />
	<link rel='stylesheet' id='elementor-frontend-css'
		href='https://kochhar.com/wp-content/plugins/elementor/assets/css/frontend.min.css?ver=3.1.4' type='text/css'
		media='all' />
	<link rel='stylesheet' id='elementor-post-9-css'
		href='https://kochhar.com/wp-content/uploads/elementor/css/post-9.css?ver=1634221151' type='text/css'
		media='all' />
	<link rel='stylesheet' id='stratum-widgets-style-css'
		href='https://kochhar.com/wp-content/plugins/stratum/assets/css/style.min.css?ver=1.3.15' type='text/css'
		media='all' />
	<link rel='stylesheet' id='elementor-pro-css'
		href='https://kochhar.com/wp-content/plugins/elementor-pro/assets/css/frontend.min.css?ver=3.1.1'
		type='text/css' media='all' />
	<link rel='stylesheet' id='elementor-global-css'
		href='https://kochhar.com/wp-content/uploads/elementor/css/global.css?ver=1634221152' type='text/css'
		media='all' />
	<link rel='stylesheet' id='ekit-widget-styles-css'
		href='https://kochhar.com/wp-content/plugins/elementskit-lite/widgets/init/assets/css/widget-styles.css?ver=3.0.2'
		type='text/css' media='all' />
	<link rel='stylesheet' id='ekit-responsive-css'
		href='https://kochhar.com/wp-content/plugins/elementskit-lite/widgets/init/assets/css/responsive.css?ver=3.0.2'
		type='text/css' media='all' />
	<link rel='stylesheet' id='cyclone-template-style-dark-0-css'
		href='https://kochhar.com/wp-content/plugins/cyclone-slider/templates/dark/style.css?ver=3.2.0' type='text/css'
		media='all' />
	<link rel='stylesheet' id='cyclone-template-style-default-0-css'
		href='https://kochhar.com/wp-content/plugins/cyclone-slider/templates/default/style.css?ver=3.2.0'
		type='text/css' media='all' />
	<link rel='stylesheet' id='cyclone-template-style-standard-0-css'
		href='https://kochhar.com/wp-content/plugins/cyclone-slider/templates/standard/style.css?ver=3.2.0'
		type='text/css' media='all' />
	<link rel='stylesheet' id='cyclone-template-style-thumbnails-0-css'
		href='https://kochhar.com/wp-content/plugins/cyclone-slider/templates/thumbnails/style.css?ver=3.2.0'
		type='text/css' media='all' />
	<link rel='stylesheet' id='google-fonts-1-css'
		href='https://fonts.googleapis.com/css?family=Roboto%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic%7CRoboto+Slab%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic&#038;ver=6.4.3'
		type='text/css' media='all' />
	<script type="text/javascript" src="https://kochhar.com/wp-includes/js/jquery/jquery.min.js?ver=3.7.1"
		id="jquery-core-js"></script>
	<script type="text/javascript" src="https://kochhar.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.4.1"
		id="jquery-migrate-js"></script>
	<link rel="https://api.w.org/" href="https://kochhar.com/wp-json/" />
	<link rel="alternate" type="application/json" href="https://kochhar.com/wp-json/wp/v2/pages/23" />
	<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://kochhar.com/xmlrpc.php?rsd" />
	<meta name="generator" content="WordPress 6.4.3" />
	<link rel='shortlink' href='https://kochhar.com/?p=23' />
	<link rel="alternate" type="application/json+oembed"
		href="https://kochhar.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fkochhar.com%2Fknowledge-centre%2F" />
	<link rel="alternate" type="text/xml+oembed"
		href="https://kochhar.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fkochhar.com%2Fknowledge-centre%2F&#038;format=xml" />
	<script>
		readMoreArgs = []
	</script>
	<script type="text/javascript">
		EXPM_VERSION=2.93;EXPM_AJAX_URL='https://kochhar.com/wp-admin/admin-ajax.php';
			function yrmAddEvent(element, eventName, fn) {
				if (element.addEventListener)
					element.addEventListener(eventName, fn, false);
				else if (element.attachEvent)
					element.attachEvent('on' + eventName, fn);
			}
	</script>
	<style type="text/css">
		.recentcomments a {
			display: inline !important;
			padding: 0 !important;
			margin: 0 !important;
		}
	</style>
	<style type="text/css">
		/************************************************************
						Style-3
		************************************************************/
		.sfwppa-navi-style.sfwppa-style-3 span.sfwppa-pages,
		.sfwppa-navi-style.sfwppa-style-3 .nav-links .prev,
		.sfwppa-navi-style.sfwppa-style-3 .nav-links .next,
		.sfwppa-navi-style.sfwppa-style-3 .sfwppa-first,
		.sfwppa-navi-style.sfwppa-style-3 .sfwppa-last {
			color: #000000;
			font-size: 14px;
		}

		.sfwppa-navi-style.sfwppa-style-3 a.sfwppa-pages:hover,
		.sfwppa-navi-style.sfwppa-style-3 .nav-links .prev:hover,
		.sfwppa-navi-style.sfwppa-style-3 .nav-links .next:hover,
		.sfwppa-navi-style.sfwppa-style-3 .nav-links .page-numbers:hover {
			color: #d1d1d1;
		}

		.sfwppa-navi-style.sfwppa-style-3 .sfwppa-link,
		.sfwppa-navi-style.sfwppa-style-3 .sfwppa-current-page,
		.sfwppa-navi-style.sfwppa-style-3 .nav-links .current,
		.sfwppa-navi-style.sfwppa-style-3 .nav-links .page-numbers {
			color: #000000;
		}

		.sfwppa-navi-style.sfwppa-style-3 .sfwppa-extend {
			color: #000000;
		}

		.sfwppa-navi-style.sfwppa-style-3 .nav-links .current {
			background: #0a306f;
			color: #ffffff;
			border: 1px solid #0a306f;
		}

		.sfwppa-navi-style.sfwppa-style-3 a.sfwppa-pages:hover,
		.sfwppa-navi-style.sfwppa-style-3 .sfwppa-link:hover,
		.sfwppa-navi-style.sfwppa-style-3 .nav-links .page-numbers:hover,
		.sfwppa-navi-style.sfwppa-style-3 .sfwppa-current-page:hover,
		.sfwppa-navi-style.sfwppa-style-3 .sfwppa-extend:hover {
			background: #0a306f;
			color: #d1d1d1;
		}
	</style>
	<link rel="icon" href="https://kochhar.com/wp-content/uploads/2021/08/cropped-Kochhar-Logo-ORGINAL-JPG-Sq-32x32.png"
		sizes="32x32" />
	<link rel="icon"
		href="https://kochhar.com/wp-content/uploads/2021/08/cropped-Kochhar-Logo-ORGINAL-JPG-Sq-192x192.png"
		sizes="192x192" />
	<link rel="apple-touch-icon"
		href="https://kochhar.com/wp-content/uploads/2021/08/cropped-Kochhar-Logo-ORGINAL-JPG-Sq-180x180.png" />
	<meta name="msapplication-TileImage"
		content="https://kochhar.com/wp-content/uploads/2021/08/cropped-Kochhar-Logo-ORGINAL-JPG-Sq-270x270.png" />
	<style type="text/css" id="wp-custom-css">
		/* Added by Milind */
		.elementor-2 .elementor-element.elementor-element-2b923e1>.elementor-widget-container {

			padding-right: 20px !important;
		}

		.our-practice-areas {
			background: url("http://kochhar.com/wp-content/uploads/2021/09/practice-areas-banner.png") no-repeat center !important;
			background-size: cover;
			height: 360px;
			border-radius: 5px 5px 0 0;
		}

		.our-industry-sectors {
			background: url("http://kochhar.com/wp-content/uploads/2021/09/industry-sector-banner.png") no-repeat center !important;
			background-size: cover;
			height: 360px;
			border-radius: 5px 5px 0 0;
		}

		.frmbtn {
			border: 1px solid #0072d8 !important;
			padding: 6px 20px 5px 20px !important;
		}

		.frmbtn:hover {
			background: #0072d8 !important;
			color: #ffffff !important;
		}

		/* Custom scollbar */
		.scroll {
			overflow-y: scroll;
			height: 450px;
			/*width: 300px;
      margin: 10px 5px; padding: 5px;*/
			text-align: justify;
		}

		.scroll::-webkit-scrollbar {
			width: 5px;
		}

		.scroll::-webkit-scrollbar-track {
			-webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0);
			border-radius: 5px;
		}

		.scroll::-webkit-scrollbar-thumb {
			border-radius: 5px;
			-webkit-box-shadow: inset 0 0 6px blue;
		}

		/* Custom end */

		/* Responsive Form */
		#responsive-form {
			max-width: 800px;
			margin: 0 auto;
			width: 100%;
		}

		.form-row {
			font-family: "Josefin Sans", Sans-serif;
			color: #505050;
			font-size: 17px;
			font-weight: 500;
			padding: 30px;
			padding-bottom: 0px;
			width: 100%;
		}

		.form-agree {
			font-size: 15px;
			margin-top: 20px;
		}

		.form-label {
			color: #0072D8;
			font-family: "Josefin Sans", Sans-serif;
			font-size: 15px;
			font-weight: 600;
			text-transform: uppercase;
			line-height: 1.4em;
			letter-spacing: 3px;
		}

		.column-full {
			float: none;
			position: relative;
			padding: 5px;
			margin: 0 2%;
			width: 100%;
			-webkit-box-sizing: border-box;
			-moz-box-sizing: border-box;
		}

		.column-half {
			float: left;
			position: relative;
			padding: 5px;
			margin: 0 2%;
			width: 46%;
			-webkit-box-sizing: border-box;
			-moz-box-sizing: border-box;
		}

		.column-quarter {
			float: left;
			position: relative;
			padding: 5px;
			margin: 0 1%;
			width: 23%;
			-webkit-box-sizing: border-box;
			-moz-box-sizing: border-box;
		}

		.clearfix:after {
			content: "";
			display: table;
			clear: both;
		}

		#form-otp {
			width: 200px;
			float: left;
			margin-right: 50px;
		}

		.wpcf7 textarea {
			height: 165px !important;
		}

		#comment-box {
			height: 122px !important;
		}

		.pum-theme-1682 .pum-title,
		.pum-theme-cutting-edge .pum-title {
			text-align: center;
			margin-bottom: 10px;
		}

		#rs-header.header-style6 .toolbar-area .toolbar-contact ul.rs-contact-info li a {
			font-weight: bold;
			color: #fff;
			font-size: 14px;
		}

		/**---------------- Media query ----------------**/
		@media only screen and (min-width: 48em) {
			/*.column-half{
width: 100%;
}*/
		}

		.wpcf7 input[type="text"],
		.wpcf7 input[type="tel"],
		.wpcf7 input[type="email"],
		.wpcf7 select,
		.wpcf7 textarea {
			/*width: 100%;*/
			padding: 8px;
			padding-bottom: 0px;
			border: 1px solid #bcbcbc !important;
			border-radius: 6px !important;
			-webkit-box-sizing: border-box;
			-moz-box-sizing: border-box;
		}

		.wpcf7 input[type="text"]:focus {
			background: #fff;
		}

		.wpcf7-submit {
			margin: 0 auto;
			text-transform: uppercase !important;
			border-radius: 4px !important;
			float: none;
			background: #ffffff !important;
			color: #000000 !important;
			text-transform: uppercase;
			border: none;
			padding: 0px 30px;
			cursor: pointer;
			width: auto;
		}

		.wpcf7-submit:hover {
			background: #00237c;
		}

		.contact-head {
			width: 100%;
			padding: 15px;
			background: #fdba11;
		}

		.contact-box {
			border: 2px solid #fdba11 !important;
			width: 100%;
			padding: 15px;
			background: #f9f9f9;
		}

		/* End Responsive form */

		/* End - Added by Milind */
		@media (min-width: 1025px) and (max-width: 1280px) {
			#mega-menu-wrap-mainmenu #mega-menu-mainmenu>li.mega-menu-item>a.mega-menu-link {
				padding: 0 18px 0 18px;
			}
		}

		.elementor-2 .elementor-element.elementor-element-b9019e4 .premium-icon-list-text span {
			color: #4C4C4C !important;
		}
	</style>
	<style type="text/css">
		/** Mega Menu CSS: fs **/
	</style>
	<script>
		jQuery(document).ready(function(){
            var width = jQuery(window).width();

            var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
            jQuery(window).scroll(function () {
                var sc = jQuery(window).scrollTop();
                //console.log(sc);
                if(width>768){
                    if (sc < 100) {
                        jQuery("#headerSectionWrapper").removeClass("wrapper1boxShadow");
                    } else {
                        jQuery("#headerSectionWrapper").addClass("wrapper1boxShadow");
                    }
                }
            });
        });
	</script>
	<!-- Global site tag (gtag.js) - Google Analytics -->
	<script async src="https://www.googletagmanager.com/gtag/js?id=G-K47V4Y9EHP"></script>
	<script>
		window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-K47V4Y9EHP');
	</script>
</head>

<body
	class="page-template page-template-template_knowledge_centre page-template-template_knowledge_centre-php page page-id-23 sfwppa-navi-style sfwppa-style-3 mega-menu-mainmenu mega-menu-footer-menu kochhar-theme elementor-default elementor-kit-9 elementor-page elementor-page-23">
	<div class="wrapper1">
		<div class="container">
			<div class="row">
				<div class="col-xl-4"></div>
				<div class="col-xl-4">
					<div class="logo"><a
							href="https://kochhar.com"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/logo2.png"></a>
					</div>
				</div>
				<div class="col-xl-4"></div>
			</div>
		</div>
	</div>
	<div class="wrapper2">
		<div class="container">
			<div class="row">
				<div class="col-xl-12">
					<div class="custommenu">
						<div id="mega-menu-wrap-mainmenu" class="mega-menu-wrap">
							<div class="mega-menu-toggle">
								<div class="mega-toggle-blocks-left"></div>
								<div class="mega-toggle-blocks-center"></div>
								<div class="mega-toggle-blocks-right">
									<div class='mega-toggle-block mega-menu-toggle-animated-block mega-toggle-block-0'
										id='mega-toggle-block-0'><button aria-label="Toggle Menu" class="mega-toggle-animated mega-toggle-animated-slider" type="button" aria-expanded="false">
                  <span class="mega-toggle-animated-box">
                    <span class="mega-toggle-animated-inner"></span>
                  </span>
                </button></div>
								</div>
							</div>
							<ul id="mega-menu-mainmenu" class="mega-menu max-mega-menu mega-menu-horizontal mega-no-js"
								data-event="hover_intent" data-effect="fade_up" data-effect-speed="200"
								data-effect-mobile="disabled" data-effect-speed-mobile="0"
								data-mobile-force-width="false" data-second-click="go" data-document-click="collapse"
								data-vertical-behaviour="standard" data-breakpoint="768" data-unbind="true"
								data-mobile-state="collapse_all" data-hover-intent-timeout="300"
								data-hover-intent-interval="100">
								<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-1214'
									id='mega-menu-item-1214'><a class="mega-menu-link"
										href="https://kochhar.com/about-us/" tabindex="0">About Us</a></li>
								<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-15'
									id='mega-menu-item-15'><a class="mega-menu-link" href="https://kochhar.com/people/"
										tabindex="0">People</a></li>
								<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-18'
									id='mega-menu-item-18'><a class="mega-menu-link"
										href="https://kochhar.com/practice-areas/" tabindex="0">Practice Areas</a></li>
								<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-21'
									id='mega-menu-item-21'><a class="mega-menu-link" href="https://kochhar.com/awards/"
										tabindex="0">Awards</a></li>
								<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-current-menu-item mega-page_item mega-page-item-23 mega-current_page_item mega-align-bottom-left mega-menu-flyout mega-menu-item-24'
									id='mega-menu-item-24'><a class="mega-menu-link"
										href="https://kochhar.com/knowledge-centre/" tabindex="0">knowledge centre</a>
								</li>
								<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-27'
									id='mega-menu-item-27'><a class="mega-menu-link" href="https://kochhar.com/media/"
										tabindex="0">Media</a></li>
								<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-30'
									id='mega-menu-item-30'><a class="mega-menu-link" href="https://kochhar.com/offices/"
										tabindex="0">Offices</a></li>
								<li class='mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-align-bottom-left mega-menu-flyout mega-menu-item-2599'
									id='mega-menu-item-2599'><a class="mega-menu-link" href="#" aria-haspopup="true"
										aria-expanded="false" tabindex="0">Get In
										Touch<span class="mega-indicator"></span></a>
									<ul class="mega-sub-menu">
										<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-2601'
											id='mega-menu-item-2601'><a class="mega-menu-link"
												href="https://kochhar.com/contact/">Contact Us</a></li>
										<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-2600'
											id='mega-menu-item-2600'><a class="mega-menu-link"
												href="https://kochhar.com/join-us/">JOIN US</a></li>
										<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-2602'
											id='mega-menu-item-2602'><a class="mega-menu-link"
												href="https://kochhar.com/alumni/">Alumni</a></li>
									</ul>
								</li>
							</ul>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="practice-areas-section2">
		<div class="practice-areas-section1 height1"></div>
		<div class="container">
			<div class="row">
				<div class="col-xl-12">
					<div class="practice-areas-wrapper"
						style="background: url('https://kochhar.com/wp-content/uploads/2021/09/Knowledge-Centre.png')">
						<h1 class="our-offices">Knowledge Centre</h1>
					</div>
				</div>
			</div>
		</div>
	</div>

	<div class="section-heading">
		<div class="container">
			<div class="row">
				<div class="col-xl-12">
					<h2>Search Filters</h2>
				</div>
			</div>
		</div>
	</div>

	<div class="container">
		<div class="search-people-section">
			<div class="search-box">
				<form id="searchForm" action="" method="get">
					<div class="row">
						<div class="col-xl-3">
							<div class="form-group">
								<input type="text" name="sq" class="form-control" placeholder="Search by keyword">
						</div>
							</div>
							<div class="col-xl-3">
								<div class="form-group">
									<select name="pa" class="form-control">
								<option value="">Practice Areas</option>
																																		<option value="1837">Aviation</option>
                                																		<option value="1190">Banking &#038; Finance</option>
                                																		<option value="1195">Competition / Antitrust</option>
                                																		<option value="1197">Corporate / M&#038;A</option>
                                																		<option value="1838">Corporate Governance, Compliance &#038; Advisory</option>
                                																		<option value="1201">Dispute Resolution</option>
                                																		<option value="1189">Intellectual Property Rights</option>
                                																		<option value="1191">International Trade Laws &#038; WTO</option>
                                																		<option value="1196">Private Equity &#038; Venture Capital</option>
                                																		<option value="1194">Private Clients, Trusts &#038; Estate Planning</option>
                                																		<option value="1203">Employment Law</option>
                                																		<option value="1198">Real Estate &#038; Construction</option>
                                																		<option value="1200">Taxation</option>
                                																		<option value="1202">TMT</option>
                                																		<option value="1204">White Collar Crime</option>
                                							</select>
								</div>
							</div>
							<div class="col-xl-3">
								<div class="form-group">
									<select name="kccat" class="form-control">
								<option value="">Category</option>
																                                    <option value="23">Alerts &amp; Updates</option>
								                                    <option value="24">Insights</option>
								                                    <option value="21">Podcast</option>
								                                    <option value="20">Publications</option>
								                                    <option value="19">Webcast</option>
															</select>
								</div>
							</div>
							<div class="col-xl-2">
								<div style="text-align: center;">
									<input type="submit" name="search" class="btn btn-primary">
						</div>
								</div>
								<div class="col-xl-1">
									<div style="text-align: center;">
										<input id="reset" type="reset" name="reset" value="Reset">
						</div>
									</div>
								</div>
				</form>
			</div>
		</div>
	</div>

	<div class="knowledge-centre-wrapper">
		<div class="container">
			<div class="row">
				<div class="col-xl-12">
					<div class="knowledge-wrapper">
						<div class="row masonry" data-target=".item" data-col-xs="12" data-col-sm="4" data-col-md="3">
							<div class="col-xs-12 col-sm-4 col-md-3">
								<div class="item">
									<div id="kc-7210" class="langbox">

										<div class="select-language">Select Language</div>

										<div class="language"><a
												href="https://kochhar.com/wp-content/uploads/2024/02/Kochhar-Co.-Bangalore.-Article-by-Lynn-Lazaro-and-Aparna-Venkat-2023-Overview-Copyright-Law-in-India-Jan-2024-.pdf"
												target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/english.png"></a>
										</div>


									</div>
									<div class="logo-section d-flex align-items-center justify-content-center">
										<img width="310" height="180" src="https://kochhar.com/wp-content/uploads/2024/02/Kochhar-and-Co-Website-2023-Overview-–-Copyright-Law-in-India-.png" class="attachment-full size-full wp-post-image" alt="" decoding="async" fetchpriority="high" srcset="https://kochhar.com/wp-content/uploads/2024/02/Kochhar-and-Co-Website-2023-Overview-–-Copyright-Law-in-India-.png 310w, https://kochhar.com/wp-content/uploads/2024/02/Kochhar-and-Co-Website-2023-Overview-–-Copyright-Law-in-India--300x174.png 300w, https://kochhar.com/wp-content/uploads/2024/02/Kochhar-and-Co-Website-2023-Overview-–-Copyright-Law-in-India--250x145.png 250w" sizes="(max-width: 310px) 100vw, 310px" />                                            										</div>

										<div class="catname">
											Insights </div>

										<div class="content-section">
											<div class="date">29 February 2024</div>
											<h5><a href="https://kochhar.com/wp-content/uploads/2024/02/Kochhar-Co.-Bangalore.-Article-by-Lynn-Lazaro-and-Aparna-Venkat-2023-Overview-Copyright-Law-in-India-Jan-2024-.pdf"
													target="_blank" rel="noopener">2023 Overview – Copyright Law in
													India</a></h5>
											<p>Author(s) &#8211; <a href="https://kochhar.com/people/lynn-lazaro/"
													target="_blank" rel="noopener">Lynn Lazaro</a>, <a
													href="https://kochhar.com/people/aparna-venkat/" target="_blank"
													rel="noopener">Aparna Venkat</a></p>
											<p>&nbsp;</p>
											<p>Jan 2024</p>

											<div class="crc-category" style="margin-top: 40px;">
												<table>
													<tr>
														<td style="width: 27px;">
															<img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/cat-icon.png"></td>
														<td>
															Intellectual Property Rights </td>
													</tr>
												</table>
											</div>
										</div>

										<div class="moreinfo"><a href="javascript:void(0)" data-boxid="kc-7210"
												data-activebtn=""><img class="morebtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/more-info.png"><img class="backbtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/back.png"></a>
										</div>
									</div>
								</div>
								<div class="col-xs-12 col-sm-4 col-md-3">
									<div class="item">
										<div id="kc-7207" class="langbox">

											<div class="select-language">Select Language</div>

											<div class="language"><a
													href="https://kochhar.com/wp-content/uploads/2024/02/Kochhar-Co.-Bangalore.-Article-by-Lynn-Lazaro-and-Aparna-Venkat-2023-OVERVIEW-–-TRADEMARK-LAW-IN-INDIA-Jan-2024-.pdf"
													target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/english.png"></a>
											</div>


										</div>
										<div class="logo-section d-flex align-items-center justify-content-center">
											<img width="310" height="180" src="https://kochhar.com/wp-content/uploads/2024/02/Kochhar-and-Co-Website-2023-Overview-–-Trademark-Law-in-India-.png" class="attachment-full size-full wp-post-image" alt="" decoding="async" srcset="https://kochhar.com/wp-content/uploads/2024/02/Kochhar-and-Co-Website-2023-Overview-–-Trademark-Law-in-India-.png 310w, https://kochhar.com/wp-content/uploads/2024/02/Kochhar-and-Co-Website-2023-Overview-–-Trademark-Law-in-India--300x174.png 300w, https://kochhar.com/wp-content/uploads/2024/02/Kochhar-and-Co-Website-2023-Overview-–-Trademark-Law-in-India--250x145.png 250w" sizes="(max-width: 310px) 100vw, 310px" />                                            										</div>

											<div class="catname">
												Insights </div>

											<div class="content-section">
												<div class="date">29 February 2024</div>
												<h5><a href="https://kochhar.com/wp-content/uploads/2024/02/Kochhar-Co.-Bangalore.-Article-by-Lynn-Lazaro-and-Aparna-Venkat-2023-OVERVIEW-%E2%80%93-TRADEMARK-LAW-IN-INDIA-Jan-2024-.pdf"
														target="_blank" rel="noopener">2023 Overview – Trademark Law in
														India</a></h5>
												<p>Author(s) &#8211; <a href="https://kochhar.com/people/lynn-lazaro/"
														target="_blank" rel="noopener">Lynn Lazaro</a>, <a
														href="https://kochhar.com/people/aparna-venkat/" target="_blank"
														rel="noopener">Aparna Venkat</a></p>
												<p>&nbsp;</p>
												<p>Jan 2024</p>

												<div class="crc-category" style="margin-top: 40px;">
													<table>
														<tr>
															<td style="width: 27px;">
																<img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/cat-icon.png"></td>
															<td>
																Intellectual Property Rights </td>
														</tr>
													</table>
												</div>
											</div>

											<div class="moreinfo"><a href="javascript:void(0)" data-boxid="kc-7207"
													data-activebtn=""><img class="morebtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/more-info.png"><img class="backbtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/back.png"></a>
											</div>
										</div>
									</div>
									<div class="col-xs-12 col-sm-4 col-md-3">
										<div class="item">
											<div id="kc-7203" class="langbox">

												<div class="select-language">Select Language</div>

												<div class="language"><a
														href="https://kochhar.com/wp-content/uploads/2024/02/Kochhar-Co.-Bangalore.-Article-by-Lynn-Lazaro-and-Arun-Babu-2023-Overview-Patent-Law-in-India-Jan-2024-.pdf"
														target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/english.png"></a>
												</div>


											</div>
											<div class="logo-section d-flex align-items-center justify-content-center">
												<img width="310" height="180" src="https://kochhar.com/wp-content/uploads/2024/02/Kochhar-and-Co-Website-2023-Overview-–-Patent-Law-in-India-.png" class="attachment-full size-full wp-post-image" alt="" decoding="async" srcset="https://kochhar.com/wp-content/uploads/2024/02/Kochhar-and-Co-Website-2023-Overview-–-Patent-Law-in-India-.png 310w, https://kochhar.com/wp-content/uploads/2024/02/Kochhar-and-Co-Website-2023-Overview-–-Patent-Law-in-India--300x174.png 300w, https://kochhar.com/wp-content/uploads/2024/02/Kochhar-and-Co-Website-2023-Overview-–-Patent-Law-in-India--250x145.png 250w" sizes="(max-width: 310px) 100vw, 310px" />                                            										</div>

												<div class="catname">
													Insights </div>

												<div class="content-section">
													<div class="date">29 February 2024</div>
													<h5><a href="https://kochhar.com/wp-content/uploads/2024/02/Kochhar-Co.-Bangalore.-Article-by-Lynn-Lazaro-and-Arun-Babu-2023-Overview-Patent-Law-in-India-Jan-2024-.pdf"
															target="_blank" rel="noopener">2023 Overview – Patent Law in
															India</a></h5>
													<p>Author(s) &#8211; <a
															href="https://kochhar.com/people/lynn-lazaro/"
															target="_blank" rel="noopener">Lynn Lazaro</a>, <a
															href="https://kochhar.com/people/arun-babu/" target="_blank"
															rel="noopener">Arun Babu</a></p>
													<p>&nbsp;</p>
													<p>Jan 2024</p>

													<div class="crc-category" style="margin-top: 40px;">
														<table>
															<tr>
																<td style="width: 27px;">
																	<img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/cat-icon.png"></td>
																<td>
																	Intellectual Property Rights </td>
															</tr>
														</table>
													</div>
												</div>

												<div class="moreinfo"><a href="javascript:void(0)" data-boxid="kc-7203"
														data-activebtn=""><img class="morebtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/more-info.png"><img class="backbtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/back.png"></a>
												</div>
											</div>
										</div>
										<div class="col-xs-12 col-sm-4 col-md-3">
											<div class="item">
												<div id="kc-7176" class="langbox">

													<div class="select-language">Select Language</div>

													<div class="language"><a
															href="https://kochhar.com/wp-content/uploads/2024/01/Kochhar-Co.-Bangalore-Employment-law-advisory-The-Karnataka-Compulsory-Gratuity-Insurance-Rules-2024-–-Key-points-.pdf"
															target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/english.png"></a>
													</div>


												</div>
												<div
													class="logo-section d-flex align-items-center justify-content-center">
													<img width="310" height="180" src="https://kochhar.com/wp-content/uploads/2024/01/Kochhar-and-Co-Website-The-Karnataka-Compulsory-Gratuity-Insurance-Rules-2024-–-Key-points-.png" class="attachment-full size-full wp-post-image" alt="Kochhar and Co Website - The Karnataka Compulsory Gratuity Insurance Rules, 2024 – Key points" decoding="async" srcset="https://kochhar.com/wp-content/uploads/2024/01/Kochhar-and-Co-Website-The-Karnataka-Compulsory-Gratuity-Insurance-Rules-2024-–-Key-points-.png 310w, https://kochhar.com/wp-content/uploads/2024/01/Kochhar-and-Co-Website-The-Karnataka-Compulsory-Gratuity-Insurance-Rules-2024-–-Key-points--300x174.png 300w, https://kochhar.com/wp-content/uploads/2024/01/Kochhar-and-Co-Website-The-Karnataka-Compulsory-Gratuity-Insurance-Rules-2024-–-Key-points--250x145.png 250w" sizes="(max-width: 310px) 100vw, 310px" />                                            										</div>

													<div class="catname">
														Insights </div>

													<div class="content-section">
														<div class="date">17 January 2024</div>
														<h5><a href="https://kochhar.com/wp-content/uploads/2024/01/Kochhar-Co.-Bangalore-Employment-law-advisory-The-Karnataka-Compulsory-Gratuity-Insurance-Rules-2024-%E2%80%93-Key-points-.pdf"
																target="_blank" rel="noopener">The Karnataka Compulsory
																Gratuity Insurance Rules, 2024 – Key points</a></h5>
														<p>Author &#8211; <a
																href="https://kochhar.com/people/debjani-aich/"
																target="_blank" rel="noopener">Debjani Aich</a></p>
														<p>&nbsp;</p>
														<p>Jan 2024</p>

														<div class="crc-category" style="margin-top: 40px;">
															<table>
																<tr>
																	<td style="width: 27px;">
																		<img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/cat-icon.png"></td>
																	<td>
																		Employment Law </td>
																</tr>
															</table>
														</div>
													</div>

													<div class="moreinfo"><a href="javascript:void(0)"
															data-boxid="kc-7176"
															data-activebtn=""><img class="morebtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/more-info.png"><img class="backbtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/back.png"></a>
													</div>
												</div>
											</div>
											<div class="col-xs-12 col-sm-4 col-md-3">
												<div class="item">
													<div id="kc-7168" class="langbox">

														<div class="select-language">Select Language</div>

														<div class="language"><a
																href="https://kochhar.com/wp-content/uploads/2024/01/Kochhar-Co.-New-Delhi.-Article-by-Kavita-Sarin-and-Vishal-Bhardwaj-The-Mediation-Act-2023-Understanding-The-Key-Features-.pdf"
																target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/english.png"></a>
														</div>


													</div>
													<div
														class="logo-section d-flex align-items-center justify-content-center">
														<img width="310" height="180" src="https://kochhar.com/wp-content/uploads/2024/01/Kochhar-and-Co-Website-The-Mediation-Act-2023-Understanding-the-Key-Feature-1-2.png" class="attachment-full size-full wp-post-image" alt="" decoding="async" />                                            										</div>

														<div class="catname">
															Insights </div>

														<div class="content-section">
															<div class="date">29 December 2023</div>
															<h5><a href="https://kochhar.com/wp-content/uploads/2024/01/Kochhar-Co.-New-Delhi.-Article-by-Kavita-Sarin-and-Vishal-Bhardwaj-The-Mediation-Act-2023-Understanding-The-Key-Features-.pdf"
																	target="_blank" rel="noopener">The Mediation Act,
																	2023: Understanding The Key Feature</a></h5>
															<p>Author(s) &#8211; <a
																	href="https://kochhar.com/people/kavita-sarin/"
																	target="_blank" rel="noopener">Kavita Sarin</a>, <a
																	href="https://kochhar.com/people/vishal-bhardwaj/"
																	target="_blank" rel="noopener">Vishal Bhardwaj</a>
															</p>
															<p>&nbsp;</p>
															<p>Dec 2023</p>

															<div class="crc-category" style="margin-top: 40px;">
																<table>
																	<tr>
																		<td style="width: 27px;">
																			<img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/cat-icon.png"></td>
																		<td>
																			Dispute Resolution </td>
																	</tr>
																</table>
															</div>
														</div>

														<div class="moreinfo"><a href="javascript:void(0)"
																data-boxid="kc-7168"
																data-activebtn=""><img class="morebtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/more-info.png"><img class="backbtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/back.png"></a>
														</div>
													</div>
												</div>
												<div class="col-xs-12 col-sm-4 col-md-3">
													<div class="item">
														<div id="kc-7131" class="langbox">

															<div class="select-language">Select Language</div>

															<div class="language"><a
																	href="https://kochhar.com/wp-content/uploads/2023/11/Kochhar-Co.-Bangalore.-Article-by-Lynn-Lazaro-and-Aparna-Venkat-Protection-of-Unregistered-Global-Brands-in-India-Nov-2023-.pdf"
																	target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/english.png"></a>
															</div>


														</div>
														<div
															class="logo-section d-flex align-items-center justify-content-center">
															<img width="310" height="180" src="https://kochhar.com/wp-content/uploads/2023/11/Kochhar-and-Co-India-Website-Protection-of-Unregistered-Global-Brands-in-India-Featured-image-.png" class="attachment-full size-full wp-post-image" alt="Kochhar and Co India Website -Protection of Unregistered Global Brands in India - Featured image" decoding="async" srcset="https://kochhar.com/wp-content/uploads/2023/11/Kochhar-and-Co-India-Website-Protection-of-Unregistered-Global-Brands-in-India-Featured-image-.png 310w, https://kochhar.com/wp-content/uploads/2023/11/Kochhar-and-Co-India-Website-Protection-of-Unregistered-Global-Brands-in-India-Featured-image--300x174.png 300w, https://kochhar.com/wp-content/uploads/2023/11/Kochhar-and-Co-India-Website-Protection-of-Unregistered-Global-Brands-in-India-Featured-image--250x145.png 250w" sizes="(max-width: 310px) 100vw, 310px" />                                            										</div>

															<div class="catname">
																Insights </div>

															<div class="content-section">
																<div class="date">29 November 2023</div>
																<h5><a href="https://kochhar.com/wp-content/uploads/2023/11/Kochhar-Co.-Bangalore.-Article-by-Lynn-Lazaro-and-Aparna-Venkat-Protection-of-Unregistered-Global-Brands-in-India-Nov-2023-.pdf"
																		target="_blank" rel="noopener">Protection of
																		Unregistered Global Brands in India</a></h5>
																<p>Author(s) &#8211; <a
																		href="https://kochhar.com/people/lynn-lazaro/"
																		target="_blank" rel="noopener">Lynn Lazaro</a>,
																	<a href="https://kochhar.com/people/aparna-venkat/"
																		target="_blank" rel="noopener">Aparna Venkat</a>
																</p>
																<p>&nbsp;</p>
																<p>Nov 2023</p>

																<div class="crc-category" style="margin-top: 40px;">
																	<table>
																		<tr>
																			<td style="width: 27px;">
																				<img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/cat-icon.png"></td>
																			<td>
																				Intellectual Property Rights </td>
																		</tr>
																	</table>
																</div>
															</div>

															<div class="moreinfo"><a href="javascript:void(0)"
																	data-boxid="kc-7131"
																	data-activebtn=""><img class="morebtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/more-info.png"><img class="backbtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/back.png"></a>
															</div>
														</div>
													</div>
													<div class="col-xs-12 col-sm-4 col-md-3">
														<div class="item">
															<div id="kc-7127" class="langbox">

																<div class="select-language">Select Language</div>

																<div class="language"><a
																		href="https://kochhar.com/wp-content/uploads/2023/11/Kochhar-Co.-Gurgaon.-Article-by-Anirudh-Mukherjee-Pankaj-Anil-Arora-Haryanas-state-law-on-employment-of-local-candidates-declared-‘unconstitutional-–-a-win-for-private-employers-.pdf"
																		target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/english.png"></a>
																</div>


															</div>
															<div
																class="logo-section d-flex align-items-center justify-content-center">
																<img width="310" height="180" src="https://kochhar.com/wp-content/uploads/2023/11/Kochhar-Co-India-Website-Haryanas-state-law-on-employment-of-local-candidates-declared-‘unconstitutional-–-a-win-for-private-employers-2-.jpg" class="attachment-full size-full wp-post-image" alt="Kochhar &amp; Co India Website - Haryana’s state law on employment of local candidates declared ‘unconstitutional’ – a win for private employers" decoding="async" srcset="https://kochhar.com/wp-content/uploads/2023/11/Kochhar-Co-India-Website-Haryanas-state-law-on-employment-of-local-candidates-declared-‘unconstitutional-–-a-win-for-private-employers-2-.jpg 310w, https://kochhar.com/wp-content/uploads/2023/11/Kochhar-Co-India-Website-Haryanas-state-law-on-employment-of-local-candidates-declared-‘unconstitutional-–-a-win-for-private-employers-2--300x174.jpg 300w, https://kochhar.com/wp-content/uploads/2023/11/Kochhar-Co-India-Website-Haryanas-state-law-on-employment-of-local-candidates-declared-‘unconstitutional-–-a-win-for-private-employers-2--250x145.jpg 250w" sizes="(max-width: 310px) 100vw, 310px" />                                            										</div>

																<div class="catname">
																	Insights </div>

																<div class="content-section">
																	<div class="date">28 November 2023</div>
																	<h5><a href="https://kochhar.com/wp-content/uploads/2023/11/Kochhar-Co.-Gurgaon.-Article-by-Anirudh-Mukherjee-Pankaj-Anil-Arora-Haryanas-state-law-on-employment-of-local-candidates-declared-%E2%80%98unconstitutional-%E2%80%93-a-win-for-private-employers-.pdf"
																			target="_blank" rel="noopener">Haryana’s
																			state law on employment of local candidates
																			declared ‘unconstitutional’ – a win for
																			private employers</a></h5>
																	<p>Author(s) &#8211; <a
																			href="https://kochhar.com/people/anirudh-mukherjee/"
																			target="_blank" rel="noopener">Anirudh
																			Mukherjee</a>, <a
																			href="https://kochhar.com/people/pankaj-anil-arora/"
																			target="_blank" rel="noopener">Pankaj
																			Arora</a></p>
																	<p>&nbsp;</p>
																	<p>Nov, 2023</p>

																	<div class="crc-category" style="margin-top: 40px;">
																		<table>
																			<tr>
																				<td style="width: 27px;">
																					<img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/cat-icon.png"></td>
																				<td>
																					Employment Law </td>
																			</tr>
																		</table>
																	</div>
																</div>

																<div class="moreinfo"><a href="javascript:void(0)"
																		data-boxid="kc-7127"
																		data-activebtn=""><img class="morebtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/more-info.png"><img class="backbtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/back.png"></a>
																</div>
															</div>
														</div>
														<div class="col-xs-12 col-sm-4 col-md-3">
															<div class="item">
																<div id="kc-7139" class="langbox">




																</div>
																<div
																	class="logo-section d-flex align-items-center justify-content-center">
																	<div
																		class="logo-section d-flex align-items-center justify-content-center kochhar-media">
																		<a data-fancybox
																			href="https://youtu.be/XlmF0Mw_fU4">
																			<img width="310" height="180" src="https://kochhar.com/wp-content/uploads/2023/11/KOCHHAR-website-Featured-image.png" class="attachment-full size-full wp-post-image" alt="YouTube Thumbnail - LegallySpeaking, a fireside chat series “Partner’s Office to GC’s Office – Journey of a Lawyer”" decoding="async" srcset="https://kochhar.com/wp-content/uploads/2023/11/KOCHHAR-website-Featured-image.png 310w, https://kochhar.com/wp-content/uploads/2023/11/KOCHHAR-website-Featured-image-300x174.png 300w, https://kochhar.com/wp-content/uploads/2023/11/KOCHHAR-website-Featured-image-250x145.png 250w" sizes="(max-width: 310px) 100vw, 310px" />
																			<img class="playbtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/play-btn.png">
                                                    </a>
																	</div>
																</div>

																<div class="catname">
																	Webcast </div>

																<div class="content-section">
																	<div class="date">8 November 2023</div>
																	<h5><a href="https://youtu.be/XlmF0Mw_fU4"
																			target="_blank"
																			rel="noopener">LegallySpeaking, a fireside
																			chat series &#8220;Partner’s Office to GC’s
																			Office – Journey of a Lawyer&#8221;</a></h5>
																	<p>Nov 2023</p>

																</div>

																<div class="moreinfo"><a href="javascript:void(0)"
																		data-boxid="kc-7139"
																		data-activebtn=""><img class="morebtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/more-info.png"><img class="backbtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/back.png"></a>
																</div>
															</div>
														</div>
														<div class="col-xs-12 col-sm-4 col-md-3">
															<div class="item">
																<div id="kc-7055" class="langbox">

																	<div class="select-language">Select Language</div>

																	<div class="language"><a
																			href="https://kochhar.com/wp-content/uploads/2023/08/Newsletter-IT-ITES-POLICY-OF-MAHARASHTRA-2023-PIVOTAL-FOR-IT-INDUSTRY-.pdf"
																			target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/english.png"></a>
																	</div>


																</div>
																<div
																	class="logo-section d-flex align-items-center justify-content-center">
																	<img width="310" height="180" src="https://kochhar.com/wp-content/uploads/2023/08/Kochhar-Co-India-Website-IT-ITes-Policy-of-Maharashtra-2023-.png" class="attachment-full size-full wp-post-image" alt="Kochhar &amp; Co India Website - IT &amp; ITes Policy of Maharashtra, 2023" decoding="async" srcset="https://kochhar.com/wp-content/uploads/2023/08/Kochhar-Co-India-Website-IT-ITes-Policy-of-Maharashtra-2023-.png 310w, https://kochhar.com/wp-content/uploads/2023/08/Kochhar-Co-India-Website-IT-ITes-Policy-of-Maharashtra-2023--300x174.png 300w, https://kochhar.com/wp-content/uploads/2023/08/Kochhar-Co-India-Website-IT-ITes-Policy-of-Maharashtra-2023--250x145.png 250w" sizes="(max-width: 310px) 100vw, 310px" />                                            										</div>

																	<div class="catname">
																		Alerts &amp; Updates </div>

																	<div class="content-section">
																		<div class="date">30 August 2023</div>
																		<h5><a href="https://kochhar.com/wp-content/uploads/2023/08/Newsletter-IT-ITES-POLICY-OF-MAHARASHTRA-2023-PIVOTAL-FOR-IT-INDUSTRY-.pdf"
																				target="_blank" rel="noopener">IT &amp;
																				ITes Policy of Maharashtra, 2023</a>
																		</h5>
																		<p>Author(s) &#8211; <a
																				href="https://kochhar.com/people/mohit-kundu/"
																				target="_blank" rel="noopener">Mohit
																				Kundu</a>, <a
																				href="https://kochhar.com/people/chandni-janyani/"
																				target="_blank" rel="noopener">Chandni
																				Janyani</a></p>
																		<p>&nbsp;</p>
																		<p>Aug, 2023</p>

																		<div class="crc-category"
																			style="margin-top: 40px;">
																			<table>
																				<tr>
																					<td style="width: 27px;">
																						<img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/cat-icon.png"></td>
																					<td>
																						Corporate Governance, Compliance
																						&#038; Advisory </td>
																				</tr>
																			</table>
																		</div>
																	</div>

																	<div class="moreinfo"><a href="javascript:void(0)"
																			data-boxid="kc-7055"
																			data-activebtn=""><img class="morebtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/more-info.png"><img class="backbtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/back.png"></a>
																	</div>
																</div>
															</div>
															<div class="col-xs-12 col-sm-4 col-md-3">
																<div class="item">
																	<div id="kc-7051" class="langbox">

																		<div class="select-language">Select Language
																		</div>

																		<div class="language"><a
																				href="https://kochhar.com/wp-content/uploads/2023/08/Kochhar-Co.-Technology-Law-Advisory-–-Digital-Personal-Data-Protection-Act-2023-.pdf"
																				target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/english.png"></a>
																		</div>


																	</div>
																	<div
																		class="logo-section d-flex align-items-center justify-content-center">
																		<img width="310" height="180" src="https://kochhar.com/wp-content/uploads/2023/08/Kochhar-and-Co-India-Website-Feature-image-Electronic-DPDP-2023-.png" class="attachment-full size-full wp-post-image" alt="Kochhar and Co India Website - Feature image - Electronic DPDP 2023" decoding="async" srcset="https://kochhar.com/wp-content/uploads/2023/08/Kochhar-and-Co-India-Website-Feature-image-Electronic-DPDP-2023-.png 310w, https://kochhar.com/wp-content/uploads/2023/08/Kochhar-and-Co-India-Website-Feature-image-Electronic-DPDP-2023--300x174.png 300w, https://kochhar.com/wp-content/uploads/2023/08/Kochhar-and-Co-India-Website-Feature-image-Electronic-DPDP-2023--250x145.png 250w" sizes="(max-width: 310px) 100vw, 310px" />                                            										</div>

																		<div class="catname">
																			Insights </div>

																		<div class="content-section">
																			<div class="date">28 August 2023</div>
																			<h5><a href="https://kochhar.com/wp-content/uploads/2023/08/Kochhar-Co.-Technology-Law-Advisory-%E2%80%93-Digital-Personal-Data-Protection-Act-2023-.pdf"
																					target="_blank"
																					rel="noopener"><strong>Technology Law Advisory – Digital Personal Data Protection Bill, 2023</strong></a>
																			</h5>
																			<p>Author(s) &#8211; <a
																					href="https://kochhar.com/people/stephen-mathias/"
																					target="_blank"
																					rel="noopener">Stephen Mathias</a>
																			</p>
																			<p>&nbsp;</p>
																			<p>Aug 2023</p>

																			<div class="crc-category"
																				style="margin-top: 40px;">
																				<table>
																					<tr>
																						<td style="width: 27px;">
																							<img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/cat-icon.png"></td>
																						<td>
																							TMT </td>
																					</tr>
																				</table>
																			</div>
																		</div>

																		<div class="moreinfo"><a
																				href="javascript:void(0)"
																				data-boxid="kc-7051"
																				data-activebtn=""><img class="morebtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/more-info.png"><img class="backbtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/back.png"></a>
																		</div>
																	</div>
																</div>
																<div class="col-xs-12 col-sm-4 col-md-3">
																	<div class="item">
																		<div id="kc-7047" class="langbox">

																			<div class="select-language">Select Language
																			</div>

																			<div class="language"><a
																					href="https://kochhar.com/wp-content/uploads/2023/08/Kochhar-Co.-Bangalore.-Article-by-Debjani-Aich-Handbook-on-Combating-Gender-Stereotypes-the-Supreme-Court-of-India-a-POV-Aug-2023.pdf"
																					target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/english.png"></a>
																			</div>


																		</div>
																		<div
																			class="logo-section d-flex align-items-center justify-content-center">
																			<img width="310" height="180" src="https://kochhar.com/wp-content/uploads/2023/08/Kochhar-and-Co-India-Website-Feature-image-Combating-Gender-Stereotypes-.png" class="attachment-full size-full wp-post-image" alt="Combating Gender Stereotypes - the Supreme Court of India - a POV" decoding="async" srcset="https://kochhar.com/wp-content/uploads/2023/08/Kochhar-and-Co-India-Website-Feature-image-Combating-Gender-Stereotypes-.png 310w, https://kochhar.com/wp-content/uploads/2023/08/Kochhar-and-Co-India-Website-Feature-image-Combating-Gender-Stereotypes--300x174.png 300w, https://kochhar.com/wp-content/uploads/2023/08/Kochhar-and-Co-India-Website-Feature-image-Combating-Gender-Stereotypes--250x145.png 250w" sizes="(max-width: 310px) 100vw, 310px" />                                            										</div>

																			<div class="catname">
																				Insights </div>

																			<div class="content-section">
																				<div class="date">28 August 2023</div>
																				<h5><a href="https://kochhar.com/wp-content/uploads/2023/08/Kochhar-Co.-Bangalore.-Article-by-Debjani-Aich-Handbook-on-Combating-Gender-Stereotypes-the-Supreme-Court-of-India-a-POV-Aug-2023.pdf"
																						target="_blank"
																						rel="noopener">Handbook on
																						Combating Gender Stereotypes
																						&#8211; the Supreme Court of
																						India &#8211; a POV</a></h5>
																				<p>Author &#8211; <a
																						href="https://kochhar.com/people/debjani-aich/"
																						target="_blank"
																						rel="noopener">Debjani Aich</a>
																				</p>
																				<p>&nbsp;</p>
																				<p>Aug 2023</p>

																				<div class="crc-category"
																					style="margin-top: 40px;">
																					<table>
																						<tr>
																							<td style="width: 27px;">
																								<img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/cat-icon.png"></td>
																							<td>
																								Employment Law </td>
																						</tr>
																					</table>
																				</div>
																			</div>

																			<div class="moreinfo"><a
																					href="javascript:void(0)"
																					data-boxid="kc-7047"
																					data-activebtn=""><img class="morebtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/more-info.png"><img class="backbtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/back.png"></a>
																			</div>
																		</div>
																	</div>
																	<div class="col-xs-12 col-sm-4 col-md-3">
																		<div class="item">
																			<div id="kc-7002" class="langbox">

																				<div class="select-language">Select
																					Language</div>

																				<div class="language"><a
																						href="https://kochhar.com/wp-content/uploads/2023/05/Kochhar-Co.-Delhi.-Article-by-Deepesh-Scope-of-Section-116-of-the-Arbitration-and-Conciliation-Act-1996-May-2023-.pdf"
																						target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/english.png"></a>
																				</div>


																			</div>
																			<div
																				class="logo-section d-flex align-items-center justify-content-center">
																				<img width="310" height="180" src="https://kochhar.com/wp-content/uploads/2023/05/Kochhar-and-Co-India-Website-Feature-image-Arbitration-and-Conciliation-Act-.png" class="attachment-full size-full wp-post-image" alt="Kochhar and Co India Website -Feature image - Arbitration and Conciliation Act" decoding="async" srcset="https://kochhar.com/wp-content/uploads/2023/05/Kochhar-and-Co-India-Website-Feature-image-Arbitration-and-Conciliation-Act-.png 310w, https://kochhar.com/wp-content/uploads/2023/05/Kochhar-and-Co-India-Website-Feature-image-Arbitration-and-Conciliation-Act--300x174.png 300w, https://kochhar.com/wp-content/uploads/2023/05/Kochhar-and-Co-India-Website-Feature-image-Arbitration-and-Conciliation-Act--250x145.png 250w" sizes="(max-width: 310px) 100vw, 310px" />                                            										</div>

																				<div class="catname">
																					Insights </div>

																				<div class="content-section">
																					<div class="date">26 May 2023</div>
																					<h5><a href="https://kochhar.com/wp-content/uploads/2023/05/Kochhar-Co.-Delhi.-Article-by-Deepesh-Scope-of-Section-116-of-the-Arbitration-and-Conciliation-Act-1996-May-2023-.pdf"
																							target="_blank"
																							rel="noopener">Scope of
																							Section 11(6) of the
																							Arbitration and Conciliation
																							Act, 1996</a></h5>
																					<p>Author &#8211; <a
																							href="https://kochhar.com/people/deepesh/"
																							target="_blank"
																							rel="noopener">Deepesh</a>
																					</p>
																					<p>&nbsp;</p>
																					<p>May 2023</p>

																					<div class="crc-category"
																						style="margin-top: 40px;">
																						<table>
																							<tr>
																								<td
																									style="width: 27px;">
																									<img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/cat-icon.png"></td>
																								<td>
																									Dispute Resolution
																								</td>
																							</tr>
																						</table>
																					</div>
																				</div>

																				<div class="moreinfo"><a
																						href="javascript:void(0)"
																						data-boxid="kc-7002"
																						data-activebtn=""><img class="morebtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/more-info.png"><img class="backbtn" src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/back.png"></a>
																				</div>
																			</div>
																		</div>
																	</div>
																	<div class="row">
																		<div class="col-xl-12">
																			<div
																				style="text-align: center; padding: 20px 0;">
																				<div class='wp-pagenavi'
																					role='navigation'>
																					<span class='sfwppa-pages'>Page 1 of 27</span><span aria-current='page' class='current'>1</span><a
																						class="sfwppa-pages sfwppa-current-page larger"
																						title="Page 2"
																						href="https://kochhar.com/knowledge-centre/page/2/">2</a><a
																						class="sfwppa-pages sfwppa-current-page larger"
																						title="Page 3"
																						href="https://kochhar.com/knowledge-centre/page/3/">3</a><a
																						class="sfwppa-pages sfwppa-current-page larger"
																						title="Page 4"
																						href="https://kochhar.com/knowledge-centre/page/4/">4</a><a
																						class="sfwppa-pages sfwppa-current-page larger"
																						title="Page 5"
																						href="https://kochhar.com/knowledge-centre/page/5/">5</a><span class='sfwppa-pages sfwppa-extend'>...</span><a
																						class="larger sfwppa-pages sfwppa-current-page"
																						title="Page 10"
																						href="https://kochhar.com/knowledge-centre/page/10/">10</a><a
																						class="larger sfwppa-pages sfwppa-current-page"
																						title="Page 20"
																						href="https://kochhar.com/knowledge-centre/page/20/">20</a><span class='sfwppa-pages sfwppa-extend'>...</span><a
																						class="sfwppa-pages sfwppa-link sfwppa-link-next"
																						rel="next"
																						aria-label="Next Page"
																						href="https://kochhar.com/knowledge-centre/page/2/">»</a><a
																						class="sfwppa-pages sfwppa-last"
																						aria-label="Last Page"
																						href="https://kochhar.com/knowledge-centre/page/27/">Last
																						»</a>
																				</div>
																			</div>
																		</div>
																	</div>
																</div>
															</div>
														</div>
													</div>
												</div>
												<script>
													jQuery(document).ready(function(){
        jQuery('.moreinfo a').click(function(){
            var boxid = jQuery(this).data("boxid");
            jQuery('#'+boxid).toggle();

            if(jQuery('#'+boxid).is(":visible")){
                jQuery(this).find(".backbtn").show();
                jQuery(this).find(".morebtn").hide();
            } else {
                jQuery(this).find(".backbtn").hide();
                jQuery(this).find(".morebtn").show();
            }
        });

        jQuery('#reset').click(function(){
            //jQuery("#searchForm")[0].reset();
            jQuery("#searchForm").trigger("reset");
            window.location.href = 'https://kochhar.com/knowledge-centre/';
        });

        jQuery('.masonry').masonry();
    });
												</script>
												<div class="wrapper3">
													<div class="container">
														<div class="row">
															<div class="col-xl-3">
																<div class="social-connects">
																	<ul>
																		<li class="follow-us">follow us</li>
																		<li><a href="https://www.facebook.com/Kochharandcompany"
																				target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/facebook.jpg"></a>
																		</li>
																		<li><a href="https://twitter.com/KochharAndCo"
																				target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/twitter.jpg"></a>
																		</li>
																		<li><a href="https://in.linkedin.com/company/kochharandco"
																				target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/linkedin.jpg"></li>
																		<li><a href="https://www.youtube.com/channel/UCW9EIAK3dcTuKhI7fvQSpsw"
																				target="_blank"><img src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/images/youtube-icon.png"></li>
																	</ul>
																</div>
															</div>
															<div class="col-xl-9">
																<div class="footer-links">
																	<div id="mega-menu-wrap-footer_menu"
																		class="mega-menu-wrap">
																		<div class="mega-menu-toggle">
																			<div class="mega-toggle-blocks-left"></div>
																			<div class="mega-toggle-blocks-center">
																			</div>
																			<div class="mega-toggle-blocks-right">
																				<div class='mega-toggle-block mega-menu-toggle-animated-block mega-toggle-block-0'
																					id='mega-toggle-block-0'><button aria-label="Toggle Menu" class="mega-toggle-animated mega-toggle-animated-slider" type="button" aria-expanded="false">
                  <span class="mega-toggle-animated-box">
                    <span class="mega-toggle-animated-inner"></span>
                  </span>
                </button></div>
																			</div>
																		</div>
																		<ul id="mega-menu-footer_menu"
																			class="mega-menu max-mega-menu mega-menu-horizontal mega-no-js"
																			data-event="hover_intent"
																			data-effect="fade_up"
																			data-effect-speed="200"
																			data-effect-mobile="disabled"
																			data-effect-speed-mobile="0"
																			data-mobile-force-width="false"
																			data-second-click="go"
																			data-document-click="collapse"
																			data-vertical-behaviour="standard"
																			data-breakpoint="768" data-unbind="true"
																			data-mobile-state="collapse_all"
																			data-hover-intent-timeout="300"
																			data-hover-intent-interval="100">
																			<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-3118'
																				id='mega-menu-item-3118'><a
																					class="mega-menu-link"
																					href="https://kochhar.com/about-us/"
																					tabindex="0">About Us</a></li>
																			<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-33'
																				id='mega-menu-item-33'><a
																					class="mega-menu-link"
																					href="https://kochhar.com/people/"
																					tabindex="0">People</a></li>
																			<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-34'
																				id='mega-menu-item-34'><a
																					class="mega-menu-link"
																					href="https://kochhar.com/practice-areas/"
																					tabindex="0">Practice Areas</a></li>
																			<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-35'
																				id='mega-menu-item-35'><a
																					class="mega-menu-link"
																					href="https://kochhar.com/awards/"
																					tabindex="0">Awards</a></li>
																			<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-current-menu-item mega-page_item mega-page-item-23 mega-current_page_item mega-align-bottom-left mega-menu-flyout mega-menu-item-36'
																				id='mega-menu-item-36'><a
																					class="mega-menu-link"
																					href="https://kochhar.com/knowledge-centre/"
																					tabindex="0">knowledge centre</a>
																			</li>
																			<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-37'
																				id='mega-menu-item-37'><a
																					class="mega-menu-link"
																					href="https://kochhar.com/media/"
																					tabindex="0">Media</a></li>
																			<li class='mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-38'
																				id='mega-menu-item-38'><a
																					class="mega-menu-link"
																					href="https://kochhar.com/offices/"
																					tabindex="0">Offices</a></li>
																		</ul>
																	</div>
																</div>
															</div>
														</div>
														<div class="row">
															<div class="col-xl-12">
																<div class="hrline"></div>
															</div>
														</div>
														<div class="row">
															<div class="col-xl-3">
																<div class="tnp tnp-subscription">
																	<!--<form method="post" action="/?na=s">
                        <input type="hidden" name="nlang" value="">
                        <input class="tnp-email" type="email" name="ne" value="" required placeholder="Email">
                        <input class="tnp-submit" type="submit" value="Subscribe" >
                    </form>-->
																	<div class="emaillist" id="es_form_f1-n1">
																		<form action="/knowledge-centre/#es_form_f1-n1"
																			method="post"
																			class="es_subscription_form es_shortcode_form "
																			id="es_subscription_form_65eb370ea639b"
																			data-source="ig-es">
																			<div class="es-field-wrap">
																				<label><input class="es_required_field es_txt_email ig_es_form_field_email" type="email" name="esfpx_email" value="" placeholder="Email" required="required" /></label>
																			</div>
																			<input type="hidden" name="esfpx_lists[]" value="3f2d9b6a59d0" /><input type="hidden" name="esfpx_form_id" value="1" /><input type="hidden" name="es" value="subscribe" />
																			<input type="hidden" name="esfpx_es_form_identifier" value="f1-n1" />
																			<input type="hidden" name="esfpx_es_email_page" value="23" />
																			<input type="hidden" name="esfpx_es_email_page_url" value="https://kochhar.com/knowledge-centre/" />
																			<input type="hidden" name="esfpx_status" value="Unconfirmed" />
																			<input type="hidden" name="esfpx_es-subscribe" id="es-subscribe-65eb370ea639b" value="b3f5bd53f7" />
																			<label style="position:absolute;top:-99999px;left:-99999px;z-index:-99;"><input type="email" name="esfpx_es_hp_email" class="es_required_field" tabindex="-1" autocomplete="-1" value="" /></label><input type="submit" name="submit" class="es_subscription_form_submit es_submit_button es_textbox_button" id="es_subscription_form_submit_65eb370ea639b" value="Subscribe" /><span class="es_spinner_image" id="spinner-image"><img src="https://kochhar.com/wp-content/plugins/email-subscribers/lite/public/images/spinner.gif" alt="Loading" /></span>
																		</form>
																		<span class="es_subscription_message " id="es_subscription_message_65eb370ea639b"></span>
																	</div>
																</div>
															</div>
															<div class="col-xl-6">
																<div class="bottom-link">
																	<ul>
																		<li><a
																				href="https://kochhar.com/alumni/">Alumni</a>
																		</li>
																		<li><a
																				href="https://kochhar.com/join-us/">Careers</a>
																		</li>
																		<li><a
																				href="https://kochhar.com/contact/#writetous">Contact</a>
																		</li>
																		<li><a
																				href="https://kochhar.com/disclaimer/">Disclaimer</a>
																		</li>
																		<li><a
																				href="https://kochhar.com/cookie/">Cookie</a>
																		</li>
																		<li><a
																				href="https://kochhar.com/privacy-policy/">Privacy
																				Policy</a></li>
																	</ul>
																</div>
															</div>
															<div class="col-xl-3">
																<div class="copyright">Copyright 2022 Kochhar & Co. All
																	rights reserved.</div>
															</div>
														</div>
													</div>
												</div>
												<script
													src="https://kochhar.com/wp-content/plugins/kochchar-co-popup/js/jq.min.js">
												</script>
												<script type=text/javascript> jQuery(document).ready(function () { let
													user=getCookie("username"); if ((user !="" ) && (user
													!="DKochharandCo" )) { } else { jQuery.jAlert({ 'title'
													: '<img class="popup-icon" src="https://kochhar.com/wp-content/plugins/kochchar-co-popup/css/KochharLogo.png" />'
													, 'content'
													: '<h3 class="popupTitle">DISCLAIMER</h3><p>The current rules of the Bar Council of India restrict / prohibit law firms from advertising and soliciting work through communication in the public domain. This website has been designed solely for the purposes of dissemination of basic information about Kochhar &amp; Co., which is made available on the specific request of the visitor/user. By clicking on &#039;AGREE&#039;, the visitor acknowledges that:</p> <ol class="descList" type="a"> <li>the contents of this website do not amount to advertising or solicitation;</li> <li>the information provided on the website is meant only for his/her understanding about our activities and who we are on their own volition;</li> <li>the contents of this website do not constitute, and shall not be construed as, legal advice or substitute for legal advice;</li> <li>the use of this website is completely at the user’s own volition and shall not create or amount to an attorney-client relationship;</li> <li>Kochhar &amp; Co. is not liable for the consequence of any action or decision taken by the visitor by relying on the contents of this website or of any external links on this website;</li> <li>Kochhar &amp; Co. does not assume any liability for the interpretation or use of the information provided on this website and does not offer any warranty, either express or implied;</li> <li>the contents of this website are the property of Kochhar &amp; Co. and the visitor is not authorised to use any part thereof, with or without adaptation, without the express prior written consent of Kochhar &amp; Co.;</li> <li>Kochhar &amp; Co., uses cookies on this website to improve user experience. By continuing to use this website without changing your privacy settings, you agree to the use of cookies.</li> </ol>'
													, 'theme' : 'custom' , 'btns' : [{ 'text' : 'Agree and Enter'
													, 'onClick' : function(){ setCookie("username", "KochharandCo" , 1);
													} }], 'size' : 'lg' , 'showAnimation' : 'fadeIn' , 'hideAnimation'
													: 'fadeOut' }); } }); </script> <style>
													.ja_body, .ja_title{ background: #ffffff !important; }
					.ja_body p, .ja_body ol{ color: #000000 !important; }
					.ja_body .ja_btn.ja_btn_default { background: #0072d8 !important; }
					.ja_body .ja_btn.ja_btn_default { color: #ffffff !important; }
					.ja_body .popupTitle { color: #0072d8 !important; }
				   </style><link rel='stylesheet' id='kochhar_co_desclaimer_popup_css2-css' href='https://kochhar.com/wp-content/plugins/kochchar-co-popup/css/popup.css?ver=1.1' type='text/css' media='all' />
<link rel='stylesheet' id='kochhar_co_desclaimer_popup_css1-css' href='https://kochhar.com/wp-content/plugins/kochchar-co-popup/css/jAlert.css?ver=1.1' type='text/css' media='all' />
<link rel='stylesheet' id='kochhar_co_desclaimer_popup_css3-css' href='https://kochhar.com/wp-content/plugins/kochchar-co-popup/css/jquery.mCustomScrollbar.css?ver=1.1' type='text/css' media='all' />
<script type="text/javascript" src="https://kochhar.com/wp-content/plugins/stratum/assets/js/editor-panel.min.js?ver=1.3.15" id="stratum-editor-panel-js-js">
												</script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-includes/js/comment-reply.min.js?ver=6.4.3"
													id="comment-reply-js" async="async" data-wp-strategy="async">
												</script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-includes/js/dist/vendor/wp-polyfill-inert.min.js?ver=3.1.2"
													id="wp-polyfill-inert-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-includes/js/dist/vendor/regenerator-runtime.min.js?ver=0.14.0"
													id="regenerator-runtime-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-includes/js/dist/vendor/wp-polyfill.min.js?ver=3.15.0"
													id="wp-polyfill-js"></script>
												<script type="text/javascript" id="contact-form-7-js-extra">
													/* <![CDATA[ */
var wpcf7 = {"api":{"root":"https:\/\/kochhar.com\/wp-json\/","namespace":"contact-form-7\/v1"}};
/* ]]> */
												</script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/contact-form-7/includes/js/index.js?ver=5.5.6.1"
													id="contact-form-7-js"></script>
												<script type="text/javascript" id="email-subscribers-js-extra">
													/* <![CDATA[ */
var es_data = {"messages":{"es_empty_email_notice":"Please enter email address","es_rate_limit_notice":"You need to wait for sometime before subscribing again","es_single_optin_success_message":"Successfully Subscribed.","es_email_exists_notice":"Email Address already exists!","es_unexpected_error_notice":"Oops.. Unexpected error occurred.","es_invalid_email_notice":"Invalid email address","es_try_later_notice":"Please try after some time"},"es_ajax_url":"https:\/\/kochhar.com\/wp-admin\/admin-ajax.php"};
/* ]]> */
												</script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/email-subscribers/lite/public/js/email-subscribers-public.js?ver=5.3.15"
													id="email-subscribers-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/js/bootstrap.bundle.min.js?ver=6.4.3"
													id="bootstrap_js-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/js/easyResponsiveTabs.js?ver=6.4.3"
													id="easyResponsiveTabs-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/js/owl.carousel.min.js?ver=6.4.3"
													id="owl_carousel_min_js-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/js/accordiom.min.js?ver=6.4.3"
													id="accordiom_min_js-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/js/bootstrap.masonry.min.js?ver=6.4.3"
													id="bootstrap_masonry_min_js-js"></script>
												<script type="text/javascript"
													src="https://cdn.jsdelivr.net/npm/@fancyapps/ui/dist/fancybox.umd.js?ver=6.4.3"
													id="jquery_fancybox_pack_js-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/js/jquery.matchHeight-min.js?ver=6.4.3"
													id="jquery_matchHeight_min_js-js"></script>
												<script type="text/javascript"
													src="//cdn.jsdelivr.net/npm/bootstrap-select@1.14.0-beta2/dist/js/bootstrap-select.min.js?ver=6.4.3"
													id="bootstrap_select_min_js-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/js/jquery.flashblue-plugins.js?ver=6.4.3"
													id="jquery_flashblue_plugins_js-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/js/jquery.sliding-tabs.js?ver=6.4.3"
													id="jquery_sliding_tabs_js-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/themes/kochhar-theme/assets/js/jquery.sliding-tabs-touch.js?ver=6.4.3"
													id="jquery_sliding_tabs_touch_js-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/elementskit-lite/libs/framework/assets/js/frontend-script.js?ver=3.0.2"
													id="elementskit-framework-js-frontend-js"></script>
												<script type="text/javascript"
													id="elementskit-framework-js-frontend-js-after">
													/* <![CDATA[ */
		var elementskit = {
			resturl: 'https://kochhar.com/wp-json/elementskit/v1/',
		}

		
/* ]]> */
												</script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/elementskit-lite/widgets/init/assets/js/widget-scripts.js?ver=3.0.2"
													id="ekit-widget-scripts-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/cyclone-slider/libs/cycle2/jquery.cycle2.min.js?ver=3.2.0"
													id="jquery-cycle2-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/cyclone-slider/libs/cycle2/jquery.cycle2.carousel.min.js?ver=3.2.0"
													id="jquery-cycle2-carousel-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/cyclone-slider/libs/cycle2/jquery.cycle2.swipe.min.js?ver=3.2.0"
													id="jquery-cycle2-swipe-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/cyclone-slider/libs/cycle2/jquery.cycle2.tile.min.js?ver=3.2.0"
													id="jquery-cycle2-tile-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/cyclone-slider/libs/cycle2/jquery.cycle2.video.min.js?ver=3.2.0"
													id="jquery-cycle2-video-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/cyclone-slider/templates/dark/script.js?ver=3.2.0"
													id="cyclone-template-script-dark-0-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/cyclone-slider/templates/thumbnails/script.js?ver=3.2.0"
													id="cyclone-template-script-thumbnails-0-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/cyclone-slider/libs/vimeo-player-js/player.js?ver=3.2.0"
													id="vimeo-player-js-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/cyclone-slider/js/client.js?ver=3.2.0"
													id="cyclone-client-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-includes/js/hoverIntent.min.js?ver=1.10.2"
													id="hoverIntent-js"></script>
												<script type="text/javascript" id="megamenu-js-extra">
													/* <![CDATA[ */
var megamenu = {"timeout":"300","interval":"100"};
/* ]]> */
												</script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/megamenu/js/maxmegamenu.js?ver=2.9.4"
													id="megamenu-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/kochchar-co-popup/js/jAlert.min.js?ver=1.1"
													id="kochhar_co_desclaimer_popup_js1-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/kochchar-co-popup/js/jAlert-functions.min.js?ver=1.2"
													id="kochhar_co_desclaimer_popup_js2-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/kochchar-co-popup/js/jquery.mCustomScrollbar.concat.min.js?ver=1.1"
													id="kochhar_co_desclaimer_popup_js3-js"></script>
												<script type="text/javascript"
													src="https://kochhar.com/wp-content/plugins/kochchar-co-popup/js/popup.js?ver=1.1"
													id="kochhar_co_desclaimer_popup_js4-js"></script>
</body>

</html>
"""

# Create a Selector object from the HTML string
selector = Selector(text=html_string)

# Use the selector to extract data
title = selector.xpath('//title/text()').get()
print("Title:", title)