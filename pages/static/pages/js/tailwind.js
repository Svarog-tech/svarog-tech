tailwind.config = {
theme: {
fontFamily: {
sans: ['Inter', 'sans-serif'],
},
extend: {
colors: {
background: '#080500', // Deep warm black
},
animation: {
'grid-move': 'grid-move 20s linear infinite',
'float': 'float 6s ease-in-out infinite',
'float-delayed': 'float 8s ease-in-out infinite reverse',
'pulse-glow': 'pulse-glow 8s ease-in-out infinite',
'pulse-glow-rev': 'pulse-glow 10s ease-in-out infinite reverse',
'reveal': 'reveal-up 1s cubic-bezier(0.16, 1, 0.3, 1) forwards',
},
keyframes: {
'grid-move': {
'0%': { backgroundPosition: '0 0' },
'100%': { backgroundPosition: '40px 40px' },
},
'float': {
'0%, 100%': { transform: 'translateY(0px) rotate(0deg)' },
'50%': { transform: 'translateY(-20px) rotate(2deg)' },
},
'pulse-glow': {
'0%, 100%': { opacity: '0.5', transform: 'scale(1)', filter: 'blur(80px)' },
'50%': { opacity: '0.8', transform: 'scale(1.1)', filter: 'blur(100px)' },
},
'reveal-up': {
'from': { opacity: '0', transform: 'translateY(30px)' },
'to': { opacity: '1', transform: 'translateY(0)' },
}
}
}
}
}