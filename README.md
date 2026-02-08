# 🏈 Super Bowl Score Prediction Game

A fun, family-friendly web application for predicting Super Bowl scores and competing with friends in real-time!

## 🎯 Overview

This interactive game lets you and your family predict the final score of Super Bowl LX (Seattle Seahawks vs New England Patriots) and compete to see who gets closest to the actual result.

## ✨ Features

### Core Functionality
- **Live Score Updates** - Automatic score updates every 60 seconds via ESPN API
- **Real-time Rankings** - Automatic leaderboard updates as scores change
- **Score Error Calculation** - Winner determined by lowest total score error
- **Manual Override** - Manual score input if API is unavailable

### User Experience
- **Confetti Celebrations** 🎉 - Animated confetti when you take the lead
- **Smooth Animations** - Staggered list animations and transitions
- **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **Dark Navy Theme** - Professional, neutral color scheme with team logos
- **Empty State Design** - Friendly onboarding for first-time users

### Game Management
- **Add Predictions** - Simple modal form with name and score inputs
- **Edit & Delete** - Three-dot menu for managing predictions
- **Auto Winner Detection** - Automatically calculates winning team from scores
- **Persistent Storage** - Predictions saved in browser localStorage
- **API Status Indicator** - Real-time connection status with retry option

### Information & Help
- **How to Play Modal** - Complete game rules and instructions
- **Team Information** - Official Seahawks and Patriots logos
- **Game Info Display** - Quarter, clock, and game status
- **Update Timestamp** - Shows how recent the data is

## 🚀 Quick Start

### Installation

No installation required! Just open the HTML file in any modern web browser:

```bash
# Clone the repository
git clone https://github.com/yourusername/superbowl-predictor.git

# Open the file
open superbowl-predictor.html
```

Or simply download `superbowl-predictor.html` and double-click to open.

### Usage

1. **Open the game** in your web browser
2. **Click "How to play"** to read the rules
3. **Add predictions** using the center button (empty state) or "+ Add" (with predictions)
4. **Watch the game** and see rankings update automatically
5. **Celebrate** when you take the lead! 🎊

## 🎮 How to Play

### Rules
1. Predict the final score for both teams
2. The player with the **lowest total score error** wins
3. Score error = `|Actual Seahawks - Predicted Seahawks| + |Actual Patriots - Predicted Patriots|`

### Example
```
Actual Score:    Seahawks 28 - 24 Patriots
Your Prediction: Seahawks 30 - 22 Patriots

Score Error: |28-30| + |24-22| = 2 + 2 = 4 points
```

### Winning
- Lower score error = Better prediction
- In case of tie, the prediction entered first wins

## 🛠️ Technical Details

### Built With
- **HTML5** - Structure
- **CSS3** - Styling and animations
- **Vanilla JavaScript** - Logic and interactivity
- **ESPN API** - Live score data
- **Canvas Confetti** - Celebration effects
- **LocalStorage** - Data persistence

### Browser Support
- Chrome (recommended)
- Firefox
- Safari
- Edge
- Any modern browser with ES6+ support

### API Integration
- Uses ESPN's public NFL scoreboard API
- Updates every 60 seconds
- Automatic retry on failure
- Manual fallback available

## 📱 Features in Detail

### Live Score System
- Fetches from ESPN API every 60 seconds
- Pauses updates when prediction modal is open
- Shows quarter, clock, and game status
- API status indicator (🟢 success, 🟡 loading, 🔴 error)
- Retry button on connection failure

### Leaderboard
- Auto-sorts by score error (lowest first)
- Winner highlighted with green background
- Slightly larger font for 1st place
- Smooth animations when rankings change
- Shows actual winning team and score error

### Predictions
- Quick add via modal form
- Auto-calculates winning team from scores
- Edit and delete via three-dot menu
- Confirmation dialog before deletion
- Persists across browser sessions

### Animations
- Confetti celebration on leader change
- Staggered slide-in for list items
- Smooth transitions on all interactions
- Floating icon in empty state
- Hover effects on all interactive elements

## 🎨 Design Philosophy

- **Minimal & Clean** - Neutral color palette
- **Sports Authentic** - Official team logos and NFL branding
- **User-Friendly** - Clear CTAs and intuitive navigation
- **Mobile-First** - Responsive grid layout
- **Accessible** - High contrast and readable fonts

## 📂 Project Structure

```
.
├── superbowl-predictor.html    # Single-file application
└── README.md                    # This file
```

## 🤝 Contributing

This is a family game project, but feel free to fork and customize for your own use!

## 📄 License

This project is open source and available under the MIT License.

## 🎉 Credits

- **NFL & ESPN** - Team logos and live score API
- **Canvas Confetti** - Confetti celebration library
- **Built with** ❤️ for Super Bowl LX

## 📞 Support

For questions or issues:
1. Check the "How to play" modal in the app
2. Use manual score input if API fails
3. Clear browser localStorage to reset

---

**Game Day:** February 8, 2026 at 6:30 PM EST
**Matchup:** Seattle Seahawks vs New England Patriots
**Location:** Levi's Stadium, Santa Clara, CA

Enjoy the game! 🏈🎉
