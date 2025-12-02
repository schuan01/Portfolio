# Portfolio Website

A modern, responsive portfolio website migrated from Flask to Svelte, based on the Trydo template's personalPortfolio design.

## Features

- ✨ Professional portfolio design from Trydo template
- 🚀 Built with Svelte 5 and TypeScript
- ⚡ Lightning-fast with Vite
- 📱 Fully responsive design
- 🎨 Complete CSS from original Trydo template
- 📧 Contact form with validation
- 🎯 Project showcase section with tabs

## Project Structure

```
Portfolio-svelte/
├── public/
│   ├── css/              # All Trydo CSS files
│   │   ├── style.css     # Main stylesheet
│   │   ├── vendor/       # Bootstrap, FontAwesome, etc.
│   │   └── plugins/      # Additional plugins
│   ├── js/               # JavaScript files
│   │   ├── main.js       # Main JS functionality
│   │   └── vendor/       # jQuery, Bootstrap, etc.
│   ├── images/           # All image assets
│   └── fonts/            # Font files
├── src/
│   ├── lib/
│   │   ├── Header.svelte      # Navigation header with social links
│   │   ├── Hero.svelte         # Hero/banner section
│   │   ├── About.svelte        # About with tabbed content
│   │   ├── Clients.svelte      # Client logos section
│   │   ├── Projects.svelte     # Portfolio projects grid
│   │   ├── Contact.svelte      # Contact form
│   │   └── Footer.svelte       # Footer with links
│   ├── App.svelte              # Main app component
│   ├── app.css                 # Custom overrides
│   └── main.ts                 # App entry point
└── index.html                  # Loads all CSS/JS from Trydo template
```

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or pnpm

### Installation

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Open your browser and navigate to `http://localhost:5173`

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run check` - Run type checking

## Customization

### Personalize Your Portfolio

1. **Hero Section** (`src/lib/Hero.svelte`):
   - Update your name, title, and description

2. **About Section** (`src/lib/About.svelte`):
   - Add your bio and update skills list

3. **Projects Section** (`src/lib/Projects.svelte`):
   - Add your projects with descriptions and links

4. **Contact Section** (`src/lib/Contact.svelte`):
   - Configure form submission (currently logs to console)

5. **Footer** (`src/lib/Footer.svelte`):
   - Update social media links

### Styling

- Global styles are in `src/app.css`
- Component-specific styles are scoped within each `.svelte` file

## Deployment

Build the project for production:

```bash
npm run build
```

The built files will be in the `dist/` directory, ready to deploy to any static hosting service like:
- Vercel
- Netlify
- GitHub Pages
- Cloudflare Pages

## Technologies Used

- **Svelte 5** - Frontend framework
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **CSS3** - Styling

## Recommended IDE Setup

[VS Code](https://code.visualstudio.com/) + [Svelte](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode)

## License

MIT License - feel free to use this template for your own portfolio!

