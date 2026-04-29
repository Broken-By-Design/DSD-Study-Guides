if (typeof DisableDevtool !== "undefined") {
    DisableDevtool({
        md5: "2cd605dd2093f27550a9503096a53e32",
        tkName: "secret",
        ondevtoolopen: (type) => {
            window.location.replace("https://www.google.com");
        },
        clearLog: true,
        disableMenu: true,
    });
}

function openGuide(pcUrl, mobileUrl) {
  const isMobile = window.innerWidth < 768;
  window.location.href = isMobile ? mobileUrl : pcUrl;
}

const html = document.documentElement;
const buttons = {
  system : document.getElementById('btn-system'),
  light  : document.getElementById('btn-light'),
  dark   : document.getElementById('btn-dark'),
};

const systemDark = window.matchMedia('(prefers-color-scheme: dark)');

function setTheme(mode) {
  Object.values(buttons).forEach(b => b.classList.remove('active'));
  buttons[mode].classList.add('active')

  if (mode === 'system') {
    html.setAttribute('data-theme', systemDark.matches ? 'dark' : 'light');
  } else {
    html.setAttribute('data-theme', mode);
  }
}

buttons.system.addEventListener('click', () => setTheme('system'));
buttons.light.addEventListener('click', () => setTheme('light'));
buttons.dark.addEventListener('click', () => setTheme('dark'));

systemDark.addEventListener('change', () => {
  if(buttons.system.classList.contains('active')) setTheme('system');
})
