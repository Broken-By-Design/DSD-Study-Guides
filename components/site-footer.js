class SiteFooter extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
      <footer class="container">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem;">
              <div>
                  <p style="margin: 0 0 0.5rem;"><strong>Made for DSD T-Level students</strong></p>
                  <p style="margin: 0 0 0.5rem; color: var(--pico-muted-color); font-size: 0.85rem;">
                      A collab between HRC DSD students <br> and Broken By Design:
                  </p>
                  <div class="collab">
                      <span class="collab-chip">Ag</span>
                      <span class="collab-chip owner"><span>Rs &lt;/b&gt;</span></span>
                  </div>
                  <div class="collab">
                      <span class="collab-chip">Tp</span>
                      <span class="collab-chip owner"><span>Vp &lt;/b&gt;</span></span>
                  </div>
              </div>
              <div>
                  <p style="margin: 0 0 0.5rem; font-size: 0.85rem; color: var(--pico-muted-color);">Theme</p>
                  <div class="segment">
                      <button id="btn-system" title="System" class="active">󰌢</button>
                      <button id="btn-light" title="Light"></button>
                      <button id="btn-dark" title="Dark"></button>
                  </div>
              </div>
          </div>
      </footer>
      `

    this.querySelector('#btn-system').addEventListener('click', () => setTheme('system'))
    this.querySelector('#btn-light').addEventListener('click', () => setTheme('light'))
    this.querySelector('#btn-dark').addEventListener('click', () => setTheme('dark'))
  }
}

customElements.define('site-footer', SiteFooter)
