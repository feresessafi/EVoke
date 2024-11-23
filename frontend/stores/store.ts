import { defineStore } from "pinia";
import { ref, computed } from "vue";
import articlesData from '@/scripts/articles_mock.json';

type ArticleStatus = 'review_needed' | 'published' | 'draft' | 'pending' | 'rejected';


interface Article {
  story_title: string;
  article_text: string;
  source_count: number;
  sources: string[];
  status: string;
  date: string;
}

interface TrendingTopic {
  name: string;
  mentions: number;
  trend: "up" | "down";
  percentage: number;
}

interface Source {
  name: string;
  count: string;
  icon: string;
  url?: string;
}

interface Stats {
  articlesInQueue: number;
  publishedToday: number;
  trendingTopicsCount: number;
  activeGenerations: number;
  readyForReview: number;
  needsAttention: number;
}

// Store
export const useStore = defineStore("store", () => {
  // State
  const articles = ref<Article[]>(articlesData);

  const isLoading = ref(false);
  const error = ref<string | null>(null);
  
  const stats = ref({
    articlesInQueue: 12,
    publishedToday: 8,
    trendingTopicsCount: 5,
    activeGenerations: 3,
    readyForReview: 8,
    needsAttention: 2,
  });

  const trendingTopics = ref<TrendingTopic[]>([
    {
      name: "Electric Vehicle Batteries",
      mentions: 342,
      trend: "up",
      percentage: 24,
    },
    {
      name: "Charging Infrastructure",
      mentions: 245,
      trend: "up",
      percentage: 18,
    },
    {
      name: "Tesla Model Updates",
      mentions: 189,
      trend: "down",
      percentage: 12,
    },
    {
      name: "EV Market Growth",
      mentions: 156,
      trend: "up",
      percentage: 15,
    },
  ]);

  const recentSources = ref<Source[]>([
    {
      name: 'Reuters EV News',
      count: '12 articles',
      icon: 'Globe',
      url: 'https://www.reuters.com/ev-news'
    },
    {
      name: 'Industry Press',
      count: '8 articles',
      icon: 'Newspaper',
      url: 'https://www.industry-press.com'
    },
    {
      name: 'Expert Comments',
      count: '5 quotes',
      icon: 'MessageSquare',
      url: 'https://www.expert-comments.com'
    }
  ]);

  // Computed
  const reviewNeededArticles = computed(() => 
    articles.value.filter(article => 
      article.status === 'Review Needed'
    )
  );

  const publishedArticles = computed(() => 
    articles.value.filter(article => article.status === 'published')
  );

  const draftArticles = computed(() => 
    articles.value.filter(article => article.status === 'draft')
  );

  // Actions
  const updateArticleStatus = (articleTitle: string, newStatus: ArticleStatus) => {
    const article = articles.value.find(a => a.story_title === articleTitle);
    if (article) {
      article.status = newStatus;
      if (newStatus === 'published') {
        stats.value.publishedToday++;
        stats.value.readyForReview--;
      } else if (newStatus === 'draft') {
        stats.value.needsAttention++;
        stats.value.readyForReview--;
      }
    }
  };

  const updateArticle = (articleTitle: string, updates: Partial<Article>) => {
    const index = articles.value.findIndex(a => a.story_title === articleTitle);
    if (index !== -1) {
      articles.value[index] = { ...articles.value[index], ...updates };
    }
  };

  const deleteArticle = (articleTitle: string) => {
    articles.value = articles.value.filter(a => a.story_title !== articleTitle);
  };

  const addArticle = (article: Article) => {
    articles.value.unshift({
      ...article,
      date: new Date().toLocaleDateString(),
    });
  };

  const updateStats = (newStats: Partial<Stats>) => {
    stats.value = { ...stats.value, ...newStats };
  };

  const updateTrendingTopics = (topics: TrendingTopic[]) => {
    trendingTopics.value = topics;
  };

  const updateRecentSources = (sources: Source[]) => {
    recentSources.value = sources;
  };

  const fetchArticles = () => {
    isLoading.value = true;
    try {
      articles.value = (articlesData || []).map(article => ({
        ...article,
        status: Math.random() > 0.5 ? "draft" : "published",
        date: new Date(Date.now() - Math.floor(Math.random() * 10) * 86400000)
          .toLocaleDateString(),
      }));
    } catch (e) {
      console.error('Error setting articles:', e);
      error.value = "Failed to set articles";
    } finally {
      isLoading.value = false;
    }
  };

  return {
    // State
    articles,
    isLoading,
    error,
    stats,
    trendingTopics,
    recentSources,

    // Computed
    reviewNeededArticles,
    publishedArticles,
    draftArticles,

    // Actions
    updateArticleStatus,
    updateArticle,
    deleteArticle,
    addArticle,
    updateStats,
    updateTrendingTopics,
    updateRecentSources,
    fetchArticles,
  };
});
