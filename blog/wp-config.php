<?php
/**
 * The base configurations of the WordPress.
 *
 * This file has the following configurations: MySQL settings, Table Prefix,
 * Secret Keys, WordPress Language, and ABSPATH. You can find more information
 * by visiting {@link http://codex.wordpress.org/Editing_wp-config.php Editing
 * wp-config.php} Codex page. You can get the MySQL settings from your web host.
 *
 * This file is used by the wp-config.php creation script during the
 * installation. You don't have to use the web site, you can just copy this file
 * to "wp-config.php" and fill in the values.
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'fishpoo1_wor0992');

/** MySQL database username */
define('DB_USER', 'fishpoo1_wor0992');

/** MySQL database password */
define('DB_PASSWORD', 'KxDG6Q5y');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY', '/[![x/@uBUd=nWO&[%sBfw[JF[IumtkafWPXu_/C<%?pttP>iicLxzez}YF]EW/QLkPE$TTCXVJE<^jb*%EG[Us};Q<eQ$!;}+$KTbbLhxcF[K!OA=@Os$]u!($>s_HI');
define('SECURE_AUTH_KEY', 'cF!zxhjr_qBhPRkD{muw?&I$|wf/qDnDLyv^?B/oj<rtN(ZkcUfOK$kEo^|c?CewVRzoz=nkW=?$tWw_b>dCxczdFNLVEV/HNpEniXfEwh};k>z>R;h_aCQx-?hByOmU');
define('LOGGED_IN_KEY', 'Lao+c_tF|Zen[wwaVQANeHwcfkQOifn|PZZ(Ul=EOqd*+q[irL]uwme}sCFeP*%n[e_kc&cTRYGV/QKv-t;MA%hs[/dT|^KlC{pd{^x@t^FQmCF^AVonNTKsuO$a?F-W');
define('NONCE_KEY', '!YfeS[Pm[I]IuPKrptu;=rGon[mDRwzj$DA@zj{&EOR%;>?C=MKz-dNvwex{BKYmktj)@P@@D>XrBJ=AW+K_;Taf[gT{nwDj_;G@DWcx^gTntCl^l]CTEYeiJw;zTZok');
define('AUTH_SALT', '-|^&CJz>sHpe^ajedRf?ZqM%!sEHYUenf&-b)U!Dx$;%Pf%Sk]f_K&X=A!PU_XO@-k$xhPk]bsTeCJukcC@l[Lr!v/WEz[GB>b|yBJ;boTXS$ncy&)c[[>Lcxvt^u|iz');
define('SECURE_AUTH_SALT', 'RxylRDCFOmy^IMLCKyKJHhnhByK*XK+XJAqH/m)t)woC@RTD_p<GeCmSlUyYzV+z[K+zf^DDkmc;H(+LgzGtLlKZ!=o!;toNkXik<v$=|lTP%vah|tG;$&GlI]>doSnf');
define('LOGGED_IN_SALT', 'hi{LcsH($]TiD@XWpf;akrIEOFI)plpAJ-S?rbmS>?;k?}O$jH=aXL=?Vv>Pr({NFnTYY@$XdU!$vf&p{sA^!tyfL>e_+{P-vfuPcaoD[p++qWlP<%rKsX|N{b@}vd>k');
define('NONCE_SALT', 'el!c@_>AtA$UU&Z%mvXyIeg}>VM*h>f+SKlpih-{UN;|^!d@{p<rG}}O{WY<xo)VrGc{WqXAIRcNZcRhqhnV]X$*B<c)j+pz|T=P>vzyW+D=<vGNw>+KRdNL>CN_/uTA');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each a unique
 * prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_ohrz_';

/**
 * WordPress Localized Language, defaults to English.
 *
 * Change this to localize WordPress. A corresponding MO file for the chosen
 * language must be installed to wp-content/languages. For example, install
 * de_DE.mo to wp-content/languages and set WPLANG to 'de_DE' to enable German
 * language support.
 */
define('WPLANG', '');

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
