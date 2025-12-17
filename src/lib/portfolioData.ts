export interface PortfolioItem {
  id: string
  title: string
  category: string
  imageClass: string
  headerBgClass: string
  headerTextColor: string
  subtitle: string
  description: string
  area: string
  platform: string
  company: string
  mainImage: string
  videoUrl?: string
  additionalImages: string[]
  customContentPath?: string
  socialLinks: {
    facebook?: string
    linkedin?: string
    instagram?: string
    twitter?: string
    steam?: string
    epic?: string
  }
}

export const portfolioData: PortfolioItem[] = [
  {
    id: 'ea-nda',
    title: 'EA NDA Project',
    category: 'Development',
    imageClass: 'image-20',
    headerBgClass: 'bg_image--20',
    headerTextColor: 'color-white',
    subtitle: 'EA NDA Project - Details coming soon.',
    description: 'EA NDA Project - Details coming soon.',
    area: 'Tech UI Lead',
    platform: 'PC, Mac, Consoles',
    company: 'Globant & EA/Maxis',
    mainImage: '/images/bg/portfolio-2.jpg',
    videoUrl: 'https://www.youtube.com/watch?v=ctsT5Y-InqE',
    additionalImages: [
      '/images/portfolio/portfolio-big-02.jpg',
      '/images/portfolio/portfolio-big-01.jpg'
    ],
    //customContentPath: '../portfolio-content/the-sims-4.html',
    socialLinks: {
      //linkedin: 'https://www.linkedin.com/company/maxis-ea/',
      //steam: 'https://store.steampowered.com/app/1222670/The_Sims_4/'
    }
  },
  {
    id: 'fortnite',
    title: 'Fortnite',
    category: 'Development',
    imageClass: 'image-7',
    headerBgClass: 'bg_image--7',
    headerTextColor: 'color-white',
    subtitle: 'Battle royale game that became a global phenomenon.',
    description: 'Fortnite is a free-to-play battle royale game where 100 players fight to be the last person standing. The game features building mechanics, regular content updates, and cross-platform play.',
    area: 'Game Development',
    platform: 'PC, Consoles, Mobile',
    company: 'Epic Games',
    mainImage: '/images/bg/fortnite-other.jpg',
    videoUrl: 'https://www.youtube.com/watch?v=ctsT5Y-InqE',
    additionalImages: [
      '/images/portfolio/portfolio-big-02.jpg',
      '/images/portfolio/portfolio-big-01.jpg'
    ],
    socialLinks: {
      epic: 'https://store.epicgames.com/es-ES/p/fortnite',
      linkedin: 'https://www.linkedin.com/company/fortnite-us/'
    }
  },
  {
    id: 'starship-troopers',
    title: 'Starship Troopers: Extermination',
    category: 'Development',
    imageClass: 'image-3',
    headerBgClass: 'bg_image--5',
    headerTextColor: 'color-white',
    subtitle: 'Cooperative FPS game based on the iconic franchise.',
    description: 'Starship Troopers: Extermination is a 16-player co-op FPS where squads of Troopers team up to battle against hordes of alien bugs. Players must work together to complete objectives and survive.',
    area: 'Game Development',
    platform: 'PC & Consoles',
    company: 'Offworld Industries',
    mainImage: '/images/bg/troopers-other.jpg',
    videoUrl: 'https://www.youtube.com/watch?v=ctsT5Y-InqE',
    additionalImages: [
      '/images/portfolio/portfolio-big-02.jpg',
      '/images/portfolio/portfolio-big-01.jpg'
    ],
    socialLinks: {
      facebook: '#',
      linkedin: '#',
      instagram: '#',
      twitter: '#',
      steam: '#'
    }
  },
  {
    id: 'dauntless',
    title: 'Dauntless',
    category: 'Development',
    imageClass: 'image-4',
    headerBgClass: 'bg_image--9',
    headerTextColor: 'color-white',
    subtitle: 'Free-to-play co-op action RPG with monster hunting gameplay.',
    description: 'Dauntless is a free-to-play online action RPG where players hunt down ferocious Behemoths. Team up with friends to take on epic boss battles and craft powerful weapons and armor.',
    area: 'Game Development',
    platform: 'PC & Consoles',
    company: 'Phoenix Labs',
    mainImage: '/images/bg/dauntless-other.jpg',
    videoUrl: 'https://www.youtube.com/watch?v=ctsT5Y-InqE',
    additionalImages: [
      '/images/portfolio/portfolio-big-02.jpg',
      '/images/portfolio/portfolio-big-01.jpg'
    ],
    socialLinks: {
      facebook: '#',
      linkedin: '#',
      instagram: '#',
      twitter: '#',
      steam: '#'
    }
  }
]

export function getPortfolioById(id: string): PortfolioItem | undefined {
  return portfolioData.find(item => item.id === id)
}
