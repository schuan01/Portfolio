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
    imageClass: 'image-8',
    headerBgClass: 'bg_image--4',
    headerTextColor: 'color-white',
    subtitle: 'EA NDA AAA Game',
    description: 'EA NDA Project - AAA Game franchise',
    area: 'Tech UI Lead',
    platform: 'PC, Mac, Consoles',
    company: 'Globant & EA',
    mainImage: '/images/bg/ea-nda-other.jpg',
    customContentPath: '../portfolio-content/ea-nda-project.html',
    socialLinks: {
    }
  },
  {
    id: 'fortnite',
    title: 'Fortnite',
    category: 'Development',
    imageClass: 'image-7',
    headerBgClass: 'bg_image--7',
    headerTextColor: 'color-white',
    subtitle: 'Massive online game created by Epic Games',
    description: 'Drop into the action you love or discover something new with your squad. Be the last player standing in Battle Royale. Get nostalgic in Fortnite OG. Go tactical in Reload. Headline Fortnite Festival. Explore the worlds of LEGO Fortnite. There is always something new for you and your friends.',
    area: 'Game Developer',
    platform: 'PC, Consoles, Mobile',
    company: 'Globant/Epic Games',
    mainImage: '/images/bg/fortnite-other.jpg',
    customContentPath: '../portfolio-content/fortnite.html',
    socialLinks: {
      epic: 'https://store.epicgames.com/en-US/p/fortnite',
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
