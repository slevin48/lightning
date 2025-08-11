import time
import streamlit as st
import streamlit.components.v1 as components

def lightning_fx(duration=2.0, count=80, emoji="⚡️"):
    ms = int(duration * 1000)
    components.html(f"""
    <script>
    (function() {{
      try {{
        const doc = window.parent && window.parent.document ? window.parent.document : document;

        // Remove any previous overlay
        const EXISTING_ID = 'emoji-fx-overlay';
        const prev = doc.getElementById(EXISTING_ID);
        if (prev) prev.remove();

        // Create full-screen overlay in the parent document
        const root = doc.createElement('div');
        root.id = EXISTING_ID;
        Object.assign(root.style, {{
          position: 'fixed',
          inset: '0',
          pointerEvents: 'none',
          zIndex: '999999'
        }});
        doc.body.appendChild(root);

        const COUNT = {count};
        const EMOJI = {emoji!r};
        const els = [];

        for (let i = 0; i < COUNT; i++) {{
          const span = doc.createElement('span');
          span.textContent = EMOJI;
          Object.assign(span.style, {{
            position: 'fixed',
            left: (Math.random() * 100) + 'vw',
            top: (-10 - Math.random() * 20) + 'vh',
            fontSize: (16 + Math.random() * 28) + 'px',
            filter: 'drop-shadow(0 0 6px rgba(255,255,80,0.7))',
            transform: 'translateY(0) rotate(0deg)',
            opacity: '0'
          }});
          root.appendChild(span);

          const sway = (Math.random() * 40 - 20);
          // Kick off transition on next frame
          requestAnimationFrame(() => {{
            span.style.transition = 'transform {duration}s linear, opacity {duration}s linear';
            span.style.transform = 'translateY(120vh) rotate(' + sway + 'deg)';
            span.style.opacity = '1';
          }});
          els.push(span);
        }}

        // Cleanup after animation
        setTimeout(() => {{
          els.forEach(el => el.remove());
          root.remove();
        }}, {ms});
      }} catch (e) {{
        console.error('emoji fx error', e);
      }}
    }})();
    </script>
    """, height=0)  # height 0 is fine now; we draw in the parent


st.title("Lightning Confetti ⚡️")
st.write("Click to celebrate with a storm of ⚡️s—like `st.balloons()` but custom!")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⚡️ Lightning!"):
        lightning_fx()
with col2:
    if st.button("🎉 Party mix"):
        # Mix a few emojis
        for e in ["⚡️","✨","💥","🔥"]:
            lightning_fx(duration=2.0, count=30, emoji=e)
            time.sleep(0.05)
with col3:
    if st.button("💡 Subtle spark"):
        lightning_fx(duration=1.2, count=25, emoji="✨")
