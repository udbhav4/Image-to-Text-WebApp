mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCoRS = false\n\
\n\
" > ~/.streamlit/config.toml
