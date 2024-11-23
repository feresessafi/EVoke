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
              Published Articles
            </h1>
            <p class="text-sm text-zinc-500 dark:text-zinc-400">
              View and manage your published content
            </p>
          </div>
          <div class="flex items-center gap-2">
            <Button variant="outline" class="gap-2">
              <ArrowDownToLine class="h-4 w-4" />
              Export Articles
            </Button>
          </div>
        </div>

        <!-- Stats Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <Card class="shadow-md hover:shadow-lg transition-shadow">
            <CardHeader class="space-y-1">
              <CardTitle class="text-sm font-medium">Total Published</CardTitle>
              <CardDescription>
                <span class="text-2xl font-bold">{{
                  publishedStats.total
                }}</span>
                <span class="text-xs text-muted-foreground ml-2">all time</span>
              </CardDescription>
            </CardHeader>
          </Card>
          <Card class="shadow-md hover:shadow-lg transition-shadow">
            <CardHeader class="space-y-1">
              <CardTitle class="text-sm font-medium">Published Today</CardTitle>
              <CardDescription>
                <span class="text-2xl font-bold text-green-600">{{
                  publishedStats.today
                }}</span>
                <span class="text-xs text-muted-foreground ml-2"
                  >+{{ publishedStats.todayIncrease }}%</span
                >
              </CardDescription>
            </CardHeader>
          </Card>

          <Card class="shadow-md hover:shadow-lg transition-shadow">
            <CardHeader>
              <CardTitle class="text-sm font-medium">Peak Engagement</CardTitle>
            </CardHeader>
            <CardContent>
              <div class="space-y-2">
                <div class="flex items-center gap-2">
                  <Clock class="h-4 w-4 text-purple-500" />
                  <span class="text-2xl font-bold">10:00</span>
                </div>
                <p class="text-xs text-muted-foreground">
                  Highest reader activity during morning hours
                </p>
              </div>
            </CardContent>
          </Card>

          <!-- Optimal Length -->
          <Card class="shadow-md hover:shadow-lg transition-shadow">
            <CardHeader>
              <CardTitle class="text-sm font-medium">Optimal Length</CardTitle>
            </CardHeader>
            <CardContent>
              <div class="space-y-2">
                <div class="flex items-center gap-2">
                  <FileText class="h-4 w-4 text-blue-500" />
                  <span class="text-2xl font-bold">1.2k</span>
                </div>
                <p class="text-xs text-muted-foreground">
                  Words for maximum engagement
                </p>
              </div>
            </CardContent>
          </Card>
        </div>

        <!-- Move Published Articles to top -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
          <!-- Articles List - Half width -->
          <Card class="shadow-md hover:shadow-lg transition-shadow">
            <CardHeader>
              <CardTitle>Published Articles</CardTitle>
              <CardDescription>Browse your published content</CardDescription>
            </CardHeader>
            <CardContent>
              <div class="space-y-4">
                <!-- Show first 5 articles with more compact design -->
                <div
                  v-for="article in publishedArticles.slice(0, 5)"
                  :key="article.story_title"
                  class="group flex items-start gap-3 p-3 bg-zinc-100 dark:bg-zinc-900 rounded-lg transition-all duration-200 ease-in-out hover:bg-white dark:hover:bg-zinc-800 hover:shadow-lg dark:hover:shadow-zinc-800/50 hover:scale-[1.02] cursor-pointer"
                  @click="openArticle(article)"
                >
                  <div class="flex-1 min-w-0">
                    <div class="flex items-center gap-2">
                      <h3
                        class="text-sm font-medium truncate group-hover:text-primary"
                      >
                        {{ article.story_title }}
                      </h3>
                      <Badge variant="default" class="text-xs">Published</Badge>
                    </div>
                    <div
                      class="flex items-center gap-3 mt-2 text-xs text-muted-foreground"
                    >
                      <span class="flex items-center gap-1">
                        <Clock class="h-3 w-3" />
                        {{ getTimeAgo(article.date) }}
                      </span>
                      <span class="flex items-center gap-1">
                        <FileText class="h-3 w-3" />
                        {{ article.article_text.split(" ").length }}
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>

          <!-- Content Performance Insights -->
          <div class="space-y-4">
            <!-- Top Topics Progress -->
            <Card class="shadow-md hover:shadow-lg transition-shadow">
              <CardHeader>
                <CardTitle>Top Topics Performance</CardTitle>
                <CardDescription
                  >Most engaging content categories</CardDescription
                >
              </CardHeader>
              <CardContent>
                <div class="space-y-4">
                  <div
                    v-for="topic in topicDistribution.slice(0, 3)"
                    :key="topic.name"
                    class="space-y-2"
                  >
                    <div class="flex items-center justify-between">
                      <div class="space-y-1">
                        <p class="text-sm font-medium">{{ topic.name }}</p>
                        <div
                          class="flex items-center gap-2 text-xs text-muted-foreground"
                        >
                          <span>{{ topic.percentage }}% coverage</span>
                          <span>•</span>
                          <span class="text-green-500"
                            >+{{ Math.floor(Math.random() * 20) }}%
                            engagement</span
                          >
                        </div>
                      </div>
                    </div>
                    <div
                      class="h-2 bg-zinc-100 dark:bg-zinc-800 rounded-full overflow-hidden"
                    >
                      <div
                        :class="['h-full', topic.color]"
                        :style="{ width: `${topic.percentage}%` }"
                      />
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            <!-- Content Quality Metrics -->
            <Card class="shadow-md hover:shadow-lg transition-shadow">
              <CardHeader>
                <CardTitle>Content Quality</CardTitle>
                <CardDescription>Key performance indicators</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="space-y-4">
                  <!-- AI Score -->
                  <div class="space-y-2">
                    <div class="flex justify-between text-sm">
                      <span class="text-muted-foreground"
                        >Average AI Score</span
                      >
                      <span class="font-medium">74%</span>
                    </div>
                    <div
                      class="h-2 bg-zinc-100 dark:bg-zinc-800 rounded-full overflow-hidden"
                    >
                      <div
                        :class="['h-full', 'bg-orange-300']"
                        :style="{ width: `74%` }"
                      />
                    </div>

                    <!-- Source Diversity -->
                    <div class="space-y-2">
                      <div class="flex justify-between text-sm">
                        <span class="text-muted-foreground"
                          >Source Diversity</span
                        >
                        <span class="font-medium">85%</span>
                      </div>
                      <div
                        class="h-2 bg-zinc-100 dark:bg-zinc-800 rounded-full overflow-hidden"
                      >
                        <div
                          :class="['h-full', 'bg-orange-500']"
                          :style="{ width: `85%` }"
                        />
                      </div>
                    </div>

                    <!-- Readability -->
                    <div class="space-y-2">
                      <div class="flex justify-between text-sm">
                        <span class="text-muted-foreground"
                          >Readability Score</span
                        >
                        <span class="font-medium">92%</span>
                      </div>
                      <div
                        class="h-2 bg-zinc-100 dark:bg-zinc-800 rounded-full overflow-hidden"
                      >
                        <div
                          :class="['h-full', 'bg-orange-700']"
                          :style="{ width: `92%` }"
                        />
                      </div>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>

        <!-- Detailed Insights Grid - Only shown when expanded -->
        <div
          v-if="showAllArticles"
          class="grid grid-cols-1 lg:grid-cols-2 gap-4"
        >
          <!-- Rest of the insight cards remain the same -->
        </div>
      </div>
    </main>

    <!-- Article Detail Modal -->
    <Dialog :open="showDetailModal" @update:open="closeDetailModal">
      <ArticleDetailModal
        v-if="selectedArticle"
        :article="selectedArticle"
        :is-open="showDetailModal"
        @close="closeDetailModal"
      />
    </Dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
import { storeToRefs } from "pinia";
import { useStore } from "@/stores/store";
import AppSidebar from "@/components/AppSidebar.vue";
import ArticleDetailModal from "@/components/ArticleDetailModal.vue";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card";
import { Dialog } from "@/components/ui/dialog";
import {
  ArrowDownToLine,
  Clock,
  FileText,
  Sparkles,
  Eye,
  PenSquare,
  Zap,
  BarChart,
  Lightbulb,
  ArrowUp,
} from "lucide-vue-next";

// Initialize store
const store = useStore();
const { publishedArticles } = storeToRefs(store);

// Mock stats data
const publishedStats = ref({
  total: 156,
  today: 12,
  todayIncrease: 15,
  avgWordCount: 1250,
  avgAiScore: 94,
});

// Modal state
const showDetailModal = ref(false);
const selectedArticle = ref(null);

const getTimeAgo = (dateString: string) => {
  const date = new Date(dateString);
  const now = new Date();
  const diffInHours = Math.floor(
    (now.getTime() - date.getTime()) / (1000 * 60 * 60)
  );

  if (diffInHours < 24) {
    return `${diffInHours}h ago`;
  }
  return `${Math.floor(diffInHours / 24)}d ago`;
};

const openArticle = (article: any) => {
  selectedArticle.value = article;
  showDetailModal.value = true;
};

const closeDetailModal = () => {
  showDetailModal.value = false;
  selectedArticle.value = null;
};

// Add these data structures
const publicationTrends = [
  { name: "Jan", count: 12 },
  { name: "Feb", count: 19 },
  { name: "Mar", count: 15 },
  { name: "Apr", count: 25 },
  { name: "May", count: 22 },
  { name: "Jun", count: 30 },
];

const maxPublications = Math.max(...publicationTrends.map((m) => m.count));

const topicDistribution = [
  { name: "Electric Vehicles", percentage: 30, color: "bg-primary" },
  { name: "Battery Tech", percentage: 25, color: "bg-blue-500" },
  { name: "Infrastructure", percentage: 20, color: "bg-yellow-500" },
  { name: "Market Analysis", percentage: 15, color: "bg-red-500" },
  { name: "Innovation", percentage: 10, color: "bg-purple-500" },
];

const recommendations = [
  {
    title: "Expand Battery Technology Coverage",
    description:
      "Articles about battery innovations show high engagement rates.",
  },
  {
    title: "Optimize Publishing Schedule",
    description:
      "Consider scheduling more posts during peak engagement hours (10:00 AM UTC).",
  },
  {
    title: "Focus on Technical Content",
    description:
      "Technical specifications in EV reviews drive more user interaction.",
  },
];

const showAllArticles = ref(false);
</script>
