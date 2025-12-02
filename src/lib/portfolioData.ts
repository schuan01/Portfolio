export interface PortfolioItem {
  id: string
  title: string
  category: string
  imageClass: string
  subtitle: string
  description: string
  branch: string
  projectType: string
  program: string
  mainImage: string
  videoUrl?: string
  additionalImages: string[]
  socialLinks: {
    facebook?: string
    linkedin?: string
    instagram?: string
    twitter?: string
  }
}

export const portfolioData: PortfolioItem[] = [
  {
    id: 'the-sims-4',
    title: 'The Sims 4',
    category: 'Development',
    imageClass: 'image-8',
    subtitle: 'A life simulation game where players create and control virtual people.',
    description: 'The Sims 4 is a life simulation game that allows players to create and control people in a virtual world. Players can customize their Sims appearance, personality, and home, and guide them through various life stages and careers.',
    branch: 'Game Development',
    projectType: 'AAA Game',
    program: 'EA Games',
    mainImage: '/images/portfolio/portfolio-big-03.jpg',
    videoUrl: 'https://www.youtube.com/watch?v=ctsT5Y-InqE',
    additionalImages: [
      '/images/portfolio/portfolio-big-02.jpg',
      '/images/portfolio/portfolio-big-01.jpg'
    ],
    socialLinks: {
      facebook: '#',
      linkedin: '#',
      instagram: '#',
      twitter: '#'
    }
  },
  {
    id: 'fortnite',
    title: 'Fortnite',
    category: 'Development',
    imageClass: 'image-7',
    subtitle: 'Battle royale game that became a global phenomenon.',
    description: 'Fortnite is a free-to-play battle royale game where 100 players fight to be the last person standing. The game features building mechanics, regular content updates, and cross-platform play.',
    branch: 'Game Development',
    projectType: 'Live Service Game',
    program: 'Epic Games',
    mainImage: '/images/portfolio/portfolio-big-03.jpg',
    videoUrl: 'https://www.youtube.com/watch?v=ctsT5Y-InqE',
    additionalImages: [
      '/images/portfolio/portfolio-big-02.jpg',
      '/images/portfolio/portfolio-big-01.jpg'
    ],
    socialLinks: {
      facebook: '#',
      linkedin: '#',
      instagram: '#',
      twitter: '#'
    }
  },
  {
    id: 'starship-troopers',
    title: 'Starship Troopers Extermination',
    category: 'Development',
    imageClass: 'image-3',
    subtitle: 'Cooperative FPS game based on the iconic franchise.',
    description: 'Starship Troopers: Extermination is a 16-player co-op FPS where squads of Troopers team up to battle against hordes of alien bugs. Players must work together to complete objectives and survive.',
    branch: 'Game Development',
    projectType: 'Multiplayer FPS',
    program: 'Offworld Industries',
    mainImage: '/images/portfolio/portfolio-big-03.jpg',
    videoUrl: 'https://www.youtube.com/watch?v=ctsT5Y-InqE',
    additionalImages: [
      '/images/portfolio/portfolio-big-02.jpg',
      '/images/portfolio/portfolio-big-01.jpg'
    ],
    socialLinks: {
      facebook: '#',
      linkedin: '#',
      instagram: '#',
      twitter: '#'
    }
  },
  {
    id: 'dauntless',
    title: 'Dauntless',
    category: 'Development',
    imageClass: 'image-4',
    subtitle: 'Free-to-play co-op action RPG with monster hunting gameplay.',
    description: 'Dauntless is a free-to-play online action RPG where players hunt down ferocious Behemoths. Team up with friends to take on epic boss battles and craft powerful weapons and armor.',
    branch: 'Game Development',
    projectType: 'Action RPG',
    program: 'Phoenix Labs',
    mainImage: '/images/portfolio/portfolio-big-03.jpg',
    videoUrl: 'https://www.youtube.com/watch?v=ctsT5Y-InqE',
    additionalImages: [
      '/images/portfolio/portfolio-big-02.jpg',
      '/images/portfolio/portfolio-big-01.jpg'
    ],
    socialLinks: {
      facebook: '#',
      linkedin: '#',
      instagram: '#',
      twitter: '#'
    }
  }
]

export function getPortfolioById(id: string): PortfolioItem | undefined {
  return portfolioData.find(item => item.id === id)
}
