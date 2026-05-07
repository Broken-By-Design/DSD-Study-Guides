#!/bin/bash
cat << 'INJECT' > temp_colors.css
/* Base / System Preferences */
:root {
  /* Default to Light Mode */
  --pico-background-color: #CAC7F6;
  --pico-card-background-color: #FFFFFF;
  --pico-color: #34454B;
  --pico-h1-color: #34454B;
  --pico-h2-color: #34454B;
  --pico-h3-color: #34454B;
  --pico-h4-color: #34454B;
  --pico-h5-color: #34454B;
  --pico-h6-color: #34454B;
  --pico-muted-color: #556c77;
  
  --pico-primary: #4C28A4;
  --pico-primary-background: #4C28A4;
  --pico-primary-border: #4C28A4;
  --pico-primary-hover: #3b1f80;
  --pico-primary-hover-background: #3b1f80;
  --pico-primary-inverse: #FFFFFF;
  
  --pico-card-border-color: rgba(52, 69, 75, 0.1);

  --tag-outline: #A09CE4;
  --tag-bg: #F6F5FF;
}

/* System Dark Mode Preference */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --pico-background-color: #181822;
    --pico-card-background-color: #242433;
    --pico-color: #EAE9F2;
    --pico-h1-color: #EAE9F2;
    --pico-h2-color: #EAE9F2;
    --pico-h3-color: #EAE9F2;
    --pico-h4-color: #EAE9F2;
    --pico-h5-color: #EAE9F2;
    --pico-h6-color: #EAE9F2;
    --pico-muted-color: #a4a2b9;
    
    --pico-primary: #6842CD;
    --pico-primary-background: #6842CD;
    --pico-primary-border: #6842CD;
    --pico-primary-hover: #7b56d6;
    --pico-primary-hover-background: #7b56d6;
    --pico-primary-inverse: #FFFFFF;
    
    --pico-card-border-color: rgba(234, 233, 242, 0.1);

    --tag-outline: #A09CE4;
    --tag-bg: rgba(160, 156, 228, 0.15);
  }
}

/* Explicit Override for Light Mode */
[data-theme="light"] {
  --pico-background-color: #CAC7F6;
  --pico-card-background-color: #FFFFFF;
  --pico-color: #34454B;
  --pico-h1-color: #34454B;
  --pico-h2-color: #34454B;
  --pico-h3-color: #34454B;
  --pico-h4-color: #34454B;
  --pico-h5-color: #34454B;
  --pico-h6-color: #34454B;
  --pico-muted-color: #556c77;
  
  --pico-primary: #4C28A4;
  --pico-primary-background: #4C28A4;
  --pico-primary-border: #4C28A4;
  --pico-primary-hover: #3b1f80;
  --pico-primary-hover-background: #3b1f80;
  --pico-primary-inverse: #FFFFFF;
  
  --pico-card-border-color: rgba(52, 69, 75, 0.1);

  --tag-outline: #A09CE4;
  --tag-bg: #F6F5FF;
}

/* Explicit Override for Dark Mode */
[data-theme="dark"] {
  --pico-background-color: #181822 !important;
  --pico-card-background-color: #242433 !important;
  --pico-color: #EAE9F2 !important;
  --pico-h1-color: #EAE9F2 !important;
  --pico-h2-color: #EAE9F2 !important;
  --pico-h3-color: #EAE9F2 !important;
  --pico-h4-color: #EAE9F2 !important;
  --pico-h5-color: #EAE9F2 !important;
  --pico-h6-color: #EAE9F2 !important;
  --pico-muted-color: #a4a2b9 !important;
  
  --pico-primary: #6842CD !important;
  --pico-primary-background: #6842CD !important;
  --pico-primary-border: #6842CD !important;
  --pico-primary-hover: #7b56d6 !important;
  --pico-primary-hover-background: #7b56d6 !important;
  --pico-primary-inverse: #FFFFFF !important;
  
  --pico-card-border-color: rgba(234, 233, 242, 0.1) !important;

  --tag-outline: #A09CE4 !important;
  --tag-bg: rgba(160, 156, 228, 0.15) !important;
}
INJECT
sed -i '' '18,80d' shared.css && cat temp_colors.css | cat - shared.css > temp && mv temp shared.css && rm temp_colors.css
