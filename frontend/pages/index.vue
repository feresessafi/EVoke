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
              Dashboard
            </h1>
            <p class="text-sm text-zinc-500 dark:text-zinc-400">
              Manage and generate articles for efahrer.com
            </p>
          </div>
          <div class="flex items-center gap-4">
            <div class="flex items-center gap-2">
              <div class="flex items-center gap-2" title="Automatically publish generated articles after review">
                <Switch v-model="autoPublish" defaultChecked />
                <Label class="text-sm text-muted-foreground">Auto-publish</Label>
              </div>
            </div>
            <!--
            <Button class="gap-2">
              <PlusCircle class="h-4 w-4" />
              New Article
            </Button>
          -->
          </div>
        </div>

        <!-- Main Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <!-- Left Column -->
          <div class="space-y-4">
            <!-- Quick Stats Row -->
            <div class="grid grid-cols-3 gap-4">
              <!-- Articles in Queue -->
              <Card>
                <CardHeader>
                  <CardTitle class="text-sm font-medium">Articles in Queue</CardTitle>
                  <div class="mt-2 flex flex-col">
                    <div class="text-2xl font-bold">{{ 8 }}</div>
                    <div class="flex items-center gap-1">
                      <ArrowUp class="h-3 w-3 text-green-500" />
                      <span class="text-xs text-muted-foreground">+3 today</span>
                    </div>
                  </div>
                </CardHeader>
              </Card>

              <!-- Published Today -->
              <Card>
                <CardHeader>
                  <CardTitle class="text-sm font-medium">Published Today</CardTitle>
                  <div class="mt-2 flex flex-col">
                    <div class="text-2xl font-bold text-green-500">{{ 5 }}</div>
                    <div class="flex items-center gap-1">
                      <Check class="h-3 w-3 text-green-500" />
                      <span class="text-xs text-muted-foreground">94% accuracy</span>
                    </div>
                  </div>
                </CardHeader>
              </Card>

              <!-- Trending Topics -->
              <Card>
                <CardHeader>
                  <CardTitle class="text-sm font-medium">Trending Topics</CardTitle>
                  <div class="mt-2 flex flex-col">
                    <div class="text-2xl font-bold text-blue-500">{{ 3 }}</div>
                    <div class="flex items-center gap-1">
                      <TrendingUp class="h-3 w-3 text-blue-500" />
                      <span class="text-xs text-muted-foreground">Active</span>
                    </div>
                  </div>
                </CardHeader>
              </Card>
            </div>

            <!-- Content Generation Card -->
            <Card>
              <CardHeader>
                <CardTitle class="text-base font-medium">Content Generation</CardTitle>
                <CardDescription>Real-time AI assistance metrics</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="space-y-4">
                  <!-- Active Generation -->
                  <div class="flex items-center space-x-4 p-3 bg-primary/5 rounded-lg border border-primary/10">
                    <div class="h-8 w-8 rounded-full bg-primary/20 flex items-center justify-center">
                      <Zap class="h-4 w-4 text-primary" />
                    </div>
                    <div class="flex-1 space-y-1">
                      <p class="text-sm font-medium">Active Generation</p>
                      <div class="flex items-center space-x-2">
                        <span class="text-2xl font-bold">3</span>
                        <span class="text-sm text-muted-foreground">in progress</span>
                      </div>
                    </div>
                  </div>

                  <!-- Quick Actions -->
                  <div class="space-y-2">
                    <div class="p-3 bg-zinc-100 dark:bg-zinc-900 rounded-lg">
                      <NuxtLink to="/review"> 
                        <div class="flex items-center justify-between">
                          <span class="text-sm font-medium flex items-center">Ready for Review <ArrowUpRight class="h-4 w-4 ml-2" /></span>
                          <Badge>{{ needsReviewCount }}</Badge>
                        </div>
                      </NuxtLink>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            <!-- Publishing Schedule Card -->
            <Card>
              <CardHeader>
                <CardTitle class="text-base font-medium">Publishing Schedule</CardTitle>
                <CardDescription>Upcoming articles</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="flex items-center justify-between space-x-2">
                  <div class="p-2 bg-zinc-100 dark:bg-zinc-900 rounded-lg flex-1">
                    <div class="flex items-center justify-between mb-1">
                      <span class="text-sm font-medium">Today <span class="text-xs text-muted-foreground ml-1">18:00</span></span>
                      <Badge class="bg-emerald-600 text-white">3</Badge>
                    </div>

                  </div>
                  <div class="p-2 bg-zinc-100 dark:bg-zinc-900 rounded-lg flex-1">
                    <div class="flex items-center justify-between mb-1">
                      <span class="text-sm font-medium">Tomorrow <span class="text-xs text-muted-foreground ml-1">8:00</span></span>
                      <Badge variant="outline">5</Badge>
                    </div>

                  </div>
                  <div class="p-2 bg-zinc-100 dark:bg-zinc-900 rounded-lg flex-1">
                    <div class="flex items-center justify-between mb-1">
                      <span class="text-sm font-medium">This Week</span>
                      <Badge variant="outline">12</Badge>
                    </div>

                  </div>
                </div>
              </CardContent>
            </Card>
          </div>

          <!-- Right Column -->
          <div class="space-y-4">

            <!-- Content Insights -->
          <Card class="">
            <CardHeader>
              <CardTitle class="text-base font-medium">Content Insights</CardTitle>
            </CardHeader>
            <CardContent class="h-[calc(100%-4rem)]">
              <div class="grid grid-cols-2 gap-2 mb-4">
                <div class="p-2 bg-zinc-100 dark:bg-zinc-900 rounded-lg">
                  <div class="flex items-center justify-between mb-1">
                    <span class="text-sm text-muted-foreground">Published</span>
                    <TrendingUp class="h-3 w-3 text-green-500" />
                  </div>
                  <p class="text-sm font-semibold">156</p>
                  <span class="text-xs text-green-500">+12 this week</span>
                </div>
                <div class="p-2 bg-zinc-100 dark:bg-zinc-900 rounded-lg">
                  <div class="flex items-center justify-between mb-1">
                    <span class="text-sm text-muted-foreground">Avg. Engagement</span>
                    <Sparkles class="h-3 w-3 text-yellow-500" />
                  </div>
                  <p class="text-sm font-semibold">94%</p>
                  <span class="text-sm text-green-500">+2.1% vs last month</span>
                </div>
              </div>
              
              <NuxtLink 
                to="/published"
                class="block p-2 bg-zinc-100 dark:bg-zinc-900 rounded-lg hover:bg-zinc-200 dark:hover:bg-zinc-800 transition-colors mt-2"
              >
                <div class="flex items-center justify-between">
                  <span class="text-sm font-semibold">View History</span>
                  <ArrowRight class="h-3 w-3" />
                </div>
              </NuxtLink>
            </CardContent>
          </Card>

            <!-- Trending Topics Card -->
            <Card>
              <CardHeader>
                <CardTitle class="text-base font-medium">Trending Topics</CardTitle>
                <CardDescription>Most discussed subjects</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="space-y-4">
                  <div v-for="topic in trendingTopics" :key="topic.name" 
                       class="p-3 bg-zinc-100 dark:bg-zinc-900 rounded-lg">
                    <div class="flex items-center gap-4">
                      <div class="flex-1 space-y-1">
                        <p class="text-sm font-medium leading-none">{{ topic.name }}</p>
                        <p class="text-sm text-muted-foreground">{{ topic.mentions }} mentions</p>
                      </div>
                      <div :class="topic.trend === 'up' ? 'text-green-500' : 'text-red-500'" class="flex items-center">
                        <TrendingUp v-if="topic.trend === 'up'" class="h-4 w-4" />
                        <TrendingDown v-else class="h-4 w-4" />
                        <span class="text-sm ml-1">{{ topic.percentage }}%</span>
                      </div>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>

        <!-- Recent Articles -->
        <div class="space-y-4">
          <div class="flex justify-between items-center">
            <h2 class="text-lg font-semibold">Recent Articles</h2>
            <Select defaultValue="all">
              <SelectTrigger class="w-32">
                <SelectValue placeholder="Filter" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">All Articles</SelectItem>
                <SelectItem value="draft">Drafts</SelectItem>
                <SelectItem value="published">Published</SelectItem>
              </SelectContent>
            </Select>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <Card
              v-for="article in articles"
              :key="article.story_title"
              class="group hover:shadow-lg transition-all duration-200 cursor-pointer border-zinc-200 dark:border-zinc-800"
              @click="handleCardClick(article)"
            >
              <CardHeader>
                <CardTitle
                  class="line-clamp-2 group-hover:text-primary transition-colors"
                >
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
                <p
                  class="text-sm text-zinc-600 dark:text-zinc-400 line-clamp-3"
                >
                  {{ article.article_text }}
                </p>
              </CardContent>
              <CardFooter
                class="flex justify-between border-t dark:border-zinc-800 pt-4"
              >
                <Button
                  variant="ghost"
                  size="sm"
                  class="opacity-0 group-hover:opacity-100 transition-opacity"
                  @click.stop="handleEdit(article)"
                >
                  <PenSquare class="h-4 w-4 mr-2" />
                  Edit
                </Button>
                <Button
                  variant="ghost"
                  size="sm"
                  class="opacity-0 group-hover:opacity-100 transition-opacity"
                  @click.stop="handlePreview(article)"
                >
                  <Eye class="h-4 w-4 mr-2" />
                  Preview
                </Button>
              </CardFooter>
            </Card>
          </div>
        </div>
      </div>
    </main>
  </div>

  <!-- Add the modal -->
  <ArticleDetailModal
    :is-open="showArticleModal"
    :article="selectedArticle"
    @close="showArticleModal = false"
    @update="handleArticleUpdate(selectedArticle, $event)"
    @delete="handleArticleDelete(selectedArticle)"
    v-if="selectedArticle"
  />
</template>

<script setup>
import { ref, watch } from "vue";
import { storeToRefs } from "pinia";
import { useStore } from "@/stores/store.ts";
import AppSidebar from "@/components/AppSidebar.vue";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "@/components/ui/card";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Progress } from "@/components/ui/progress";
import { Badge } from "@/components/ui/badge";
import {
  PlusCircle,
  PenSquare,
  Eye,
  TrendingUp,
  TrendingDown,
  Zap,
  ArrowUp,
  ArrowUpRight,
  Check,
  ArrowRight
} from "lucide-vue-next";
import ArticleDetailModal from "@/components/ArticleDetailModal.vue";
import { Switch } from "@/components/ui/switch";
import { Label } from "@/components/ui/label";
import { getStatusVariant, formatStatus } from '@/utils/status';

// Initialize store
const store = useStore();
const { articles, isLoading, error, trendingTopics, recentSources } =
  storeToRefs(store);

const needsAttentionCount = computed(() => {
  return store.articles.filter(article => article.status === 'draft').length;
});

const needsReviewCount = computed(() => {
  return store.articles.filter(article => article.status === 'Review Needed').length;
});
// State variables for modal
const showArticleModal = ref(false);
const selectedArticle = ref(null);

// Add state for auto-publish
const autoPublish = ref(true);

// Add a watch if you want to handle changes
watch(autoPublish, (newValue) => {
  console.log('Auto-publish:', newValue);
  // Here you can add logic to handle auto-publish state changes
});

// Handler for article updates
const handleArticleUpdate = (article, updates) => {
  store.updateArticle(article.story_title, updates);
};

// Handler for article deletion
const handleArticleDelete = (article) => {
  store.deleteArticle(article.story_title);
  showArticleModal.value = false;
};

// Add these functions to your script setup
const handleEdit = (article) => {
  selectedArticle.value = article;
  showArticleModal.value = true;
};

const handlePreview = (article) => {
  if (article.sources && article.sources.length > 0) {
    window.open(article.sources[0], "_blank");
  }
};

const handleCardClick = (article) => {
  selectedArticle.value = article;
  showArticleModal.value = true;
};
</script>
