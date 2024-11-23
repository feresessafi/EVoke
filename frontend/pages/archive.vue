<template>
  <div class="flex h-screen bg-zinc-50 dark:bg-zinc-950">
    <AppSidebar />

    <!-- Main Content -->
    <main class="flex-1 overflow-auto">
      <div class="p-6 space-y-6">
        <!-- Header Section -->
        <div class="flex justify-between items-center">
          <div>
            <h1 class="text-2xl font-bold text-zinc-900 dark:text-zinc-50">
              Article Archive
            </h1>
            <p class="text-sm text-zinc-500 dark:text-zinc-400">
              Browse and search all articles
            </p>
          </div>
          <div class="flex items-center gap-2">
            <!-- Search -->
            <div class="relative w-64">
              <Search class="absolute left-2 top-2.5 h-4 w-4 text-muted-foreground" />
              <Input
                v-model="searchQuery"
                placeholder="Search articles..."
                class="pl-8"
              />
            </div>
            <!-- Filter -->
            <Select v-model="filterStatus">
              <SelectTrigger class="w-32">
                <SelectValue placeholder="Status" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">All Status</SelectItem>
                <SelectItem value="published">Published</SelectItem>
                <SelectItem value="draft">Draft</SelectItem>
                <SelectItem value="review_needed">Review Needed</SelectItem>
              </SelectContent>
            </Select>
            <!-- Sort -->
            <Select v-model="sortBy">
              <SelectTrigger class="w-40">
                <SelectValue placeholder="Sort by" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="date-desc">Newest First</SelectItem>
                <SelectItem value="date-asc">Oldest First</SelectItem>
                <SelectItem value="title">Title A-Z</SelectItem>
              </SelectContent>
            </Select>
          </div>
        </div>

        <!-- Articles Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <Card
            v-for="article in filteredAndSortedArticles"
            :key="article.story_title"
            class="group hover:shadow-lg transition-all duration-200 cursor-pointer"
            @click="handleArticleClick(article)"
          >
            <CardHeader>
              <CardTitle class="line-clamp-2 group-hover:text-primary transition-colors">
                {{ article.story_title }}
              </CardTitle>
              <CardDescription class="flex items-center gap-2 mt-2">
                <Badge :variant="getStatusVariant(article.status)">
                  {{ formatStatus(article.status) }}
                </Badge>
                <span class="text-xs">{{ article.date }}</span>
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p class="text-sm text-zinc-600 dark:text-zinc-400 line-clamp-3">
                {{ article.article_text }}
              </p>
            </CardContent>
            <CardFooter class="flex justify-between border-t dark:border-zinc-800 pt-4">
              <div class="flex items-center gap-2 text-sm text-muted-foreground">
                <FileText class="h-4 w-4" />
                {{ article.article_text.split(' ').length }} words
              </div>
              <div class="flex gap-2">
                <Button
                  variant="ghost"
                  size="sm"
                  class="opacity-0 group-hover:opacity-100 transition-opacity"
                  @click.stop="handlePreview(article)"
                >
                  <Eye class="h-4 w-4 mr-2" />
                  Preview
                </Button>
              </div>
            </CardFooter>
          </Card>
        </div>
      </div>
    </main>

    <!-- Article Detail Modal -->
    <ArticleDetailModal
      :is-open="showArticleModal"
      :article="selectedArticle"
      @close="showArticleModal = false"
      v-if="selectedArticle"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { storeToRefs } from 'pinia';
import { useStore } from '@/stores/store';
import AppSidebar from '@/components/AppSidebar.vue';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from '@/components/ui/card';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { Search, Eye, FileText } from 'lucide-vue-next';
import ArticleDetailModal from '@/components/ArticleDetailModal.vue';
import { getStatusVariant, formatStatus } from '@/utils/status';

// Initialize store
const store = useStore();
const { articles } = storeToRefs(store);

// State
const searchQuery = ref('');
const filterStatus = ref('all');
const sortBy = ref('date-desc');
const showArticleModal = ref(false);
const selectedArticle = ref(null);

// Computed
const filteredAndSortedArticles = computed(() => {
  let filtered = articles.value;

  // Apply status filter
  if (filterStatus.value !== 'all') {
    filtered = filtered.filter(article => article.status === filterStatus.value);
  }

  // Apply search filter
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase();
    filtered = filtered.filter(article => 
      article.story_title.toLowerCase().includes(query) ||
      article.article_text.toLowerCase().includes(query)
    );
  }

  // Apply sorting
  return [...filtered].sort((a, b) => {
    switch (sortBy.value) {
      case 'date-desc':
        return new Date(b.date).getTime() - new Date(a.date).getTime();
      case 'date-asc':
        return new Date(a.date).getTime() - new Date(b.date).getTime();
      case 'title':
        return a.story_title.localeCompare(b.story_title);
      default:
        return 0;
    }
  });
});

// Handlers
const handleArticleClick = (article: any) => {
  selectedArticle.value = article;
  showArticleModal.value = true;
};

const handlePreview = (article: any) => {
  if (article.sources && article.sources.length > 0) {
    window.open(article.sources[0], '_blank');
  }
};
</script>