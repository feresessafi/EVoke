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
              Review Queue
            </h1>
            <p class="text-sm text-zinc-500 dark:text-zinc-400">
              Review and approve AI-generated articles
            </p>
          </div>
          <div class="flex items-center gap-2">
            <Button variant="outline" class="gap-2">
              <ArrowDownToLine class="h-4 w-4" />
              Export Report
            </Button>
          </div>
        </div>

        <!-- Review Stats -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <Card class="shadow-md hover:shadow-lg transition-shadow">
            <CardHeader class="space-y-1">
              <CardTitle class="text-sm font-medium">Pending Review</CardTitle>
              <CardDescription>
                <span class="text-2xl font-bold">{{
                  reviewStats.pending
                }}</span>
                <span class="text-xs text-muted-foreground ml-2">+3 today</span>
              </CardDescription>
            </CardHeader>
          </Card>
          <Card class="shadow-md hover:shadow-lg transition-shadow">
            <CardHeader class="space-y-1">
              <CardTitle class="text-sm font-medium">Approved Today</CardTitle>
              <CardDescription>
                <span class="text-2xl font-bold text-green-600">{{
                  reviewStats.approved
                }}</span>
                <span class="text-xs text-muted-foreground ml-2"
                  >94% accuracy</span
                >
              </CardDescription>
            </CardHeader>
          </Card>
          <Card class="shadow-md hover:shadow-lg transition-shadow">
            <CardHeader class="space-y-1">
              <CardTitle class="text-sm font-medium">Needs Revision</CardTitle>
              <CardDescription>
                <span class="text-2xl font-bold text-yellow-600">{{
                  reviewStats.needsRevision
                }}</span>
                <span class="text-xs text-muted-foreground ml-2"
                  >-2 from yesterday</span
                >
              </CardDescription>
            </CardHeader>
          </Card>
          <Card class="shadow-md hover:shadow-lg transition-shadow">
            <CardHeader class="space-y-1">
              <CardTitle class="text-sm font-medium"
                >Avg. Review Time</CardTitle
              >
              <CardDescription>
                <span class="text-2xl font-bold">4.2</span>
                <span class="text-xs text-muted-foreground ml-2">minutes</span>
              </CardDescription>
            </CardHeader>
          </Card>
        </div>

        <!-- Review Queue Table -->
        <Card class="shadow-md hover:shadow-lg transition-shadow">
          <CardHeader>
            <CardTitle>Articles Queue</CardTitle>
            <CardDescription
              >Review and manage generated articles</CardDescription
            >
          </CardHeader>
          <CardContent>
            <div class="space-y-4">
              <div
                v-for="article in filteredArticles"
                :key="article.story_title"
                class="group flex items-start gap-4 p-4 bg-zinc-100 dark:bg-zinc-900 rounded-lg transition-all duration-200 ease-in-out hover:bg-white dark:hover:bg-zinc-800 hover:shadow-lg dark:hover:shadow-zinc-800/50 hover:scale-[1.02] cursor-pointer"
                @click="openArticle(article)"
              >
                <!-- Status Indicator -->
                <div class="mt-1">
                  <div
                    :class="{
                      'w-3 h-3 rounded-full transition-colors duration-200': true,
                      'bg-yellow-500 group-hover:bg-yellow-600':
                        article.status === 'review_needed',
                      'bg-green-500 group-hover:bg-green-600':
                        article.status === 'published',
                      'bg-red-500 group-hover:bg-red-600':
                        article.status === 'draft',
                    }"
                  ></div>
                </div>

                <!-- Article Info -->
                <div class="flex-1 min-w-0">
                  <div class="flex items-center gap-2">
                    <h3 class="font-medium truncate group-hover:text-primary">
                      {{ article.story_title }}
                    </h3>
                    <Badge
                      :variant="getStatusVariant(article.status)"
                      class="transition-colors duration-200"
                    >
                      {{ formatStatus(article.status) }}
                    </Badge>
                  </div>
                  <p
                    class="text-sm text-muted-foreground line-clamp-2 mt-1 group-hover:text-zinc-700 dark:group-hover:text-zinc-300"
                  >
                    {{ article.article_text }}
                  </p>
                  <div
                    class="flex items-center gap-4 mt-2 text-sm text-muted-foreground"
                  >
                    <span
                      class="flex items-center gap-1 group-hover:text-zinc-700 dark:group-hover:text-zinc-300"
                    >
                      <Clock class="h-3 w-3" />
                      {{ article.timeAgo }}
                    </span>
                    <span
                      class="flex items-center gap-1 group-hover:text-zinc-700 dark:group-hover:text-zinc-300"
                    >
                      <FileText class="h-3 w-3" />
                      {{ article.wordCount }} words
                    </span>
                    <span
                      class="flex items-center gap-1 group-hover:text-zinc-700 dark:group-hover:text-zinc-300"
                    >
                      <Sparkles class="h-3 w-3" />
                      {{ article.aiScore }}% AI Score
                    </span>
                  </div>
                </div>

                <!-- Action Buttons -->
                <div
                  class="flex items-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity duration-200"
                >
                  <Button
                    variant="ghost"
                    size="sm"
                    @click="openArticle(article)"
                    class="hover:bg-zinc-200 dark:hover:bg-zinc-700"
                  >
                    <Eye class="h-4 w-4" />
                  </Button>
                  <Button
                    variant="ghost"
                    size="sm"
                    @click="approveArticle(article)"
                    class="hover:bg-green-100 dark:hover:bg-green-900/30 hover:text-green-600"
                  >
                    <Check class="h-4 w-4" />
                  </Button>
                  <Button
                    variant="ghost"
                    size="sm"
                    @click="rejectArticle(article)"
                    class="hover:bg-red-100 dark:hover:bg-red-900/30 hover:text-red-600"
                  >
                    <X class="h-4 w-4" />
                  </Button>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </main>

    <!-- Article Review Modal -->
    <Dialog :open="showReviewModal" @update:open="closeReviewModal">
      <ArticleReviewModal
        v-if="selectedArticle"
        :article="selectedArticle"
        @close="closeReviewModal"
        @approve="approveArticle"
        @reject="rejectArticle"
      />
    </Dialog>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { storeToRefs } from "pinia";
import { useStore } from "@/stores/store";
import AppSidebar from "@/components/AppSidebar.vue";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Dialog, DialogContent } from "@/components/ui/dialog";
import {
  ArrowDownToLine,
  Clock,
  FileText,
  Sparkles,
  Eye,
  Check,
  X,
} from "lucide-vue-next";
import { getStatusVariant, formatStatus } from "@/utils/status";
import ArticleReviewModal from "@/components/ArticleReviewModal.vue";

// Initialize store
const store = useStore();
const { articles, reviewNeededArticles } = storeToRefs(store);

// Stats computed from store data
const reviewStats = computed(() => ({
  pending: reviewNeededArticles.value.length,
  approved: articles.value.filter((a) => a.status === "published").length,
  needsRevision: articles.value.filter((a) => a.status === "draft").length,
}));

const filterStatus = ref("all");
const showReviewModal = ref(false);
const selectedArticle = ref(null);

// Filter articles based on status
const filteredArticles = computed(() => {
  const articlesForReview = reviewNeededArticles.value.map((article) => ({
    ...article,
    wordCount: article.article_text.split(" ").length,
    timeAgo: getTimeAgo(article.date),
    aiScore: Math.floor(Math.random() * 10) + 90, // Mock AI score between 90-100
  }));

  if (filterStatus.value === "all") return articlesForReview;
  return articlesForReview.filter(
    (article) => article.status === filterStatus.value
  );
});

// Helper function to calculate time ago
const getTimeAgo = (dateString) => {
  const date = new Date(dateString);
  const now = new Date();
  const diffInHours = Math.floor((now - date) / (1000 * 60 * 60));

  if (diffInHours < 24) {
    return `${diffInHours}h ago`;
  }
  return `${Math.floor(diffInHours / 24)}d ago`;
};

const openArticle = (article) => {
  selectedArticle.value = article;
  showReviewModal.value = true;
};

const approveArticle = (article) => {
  store.updateArticleStatus(article.story_title, "published");
};

const rejectArticle = (article) => {
  store.updateArticleStatus(article.story_title, "draft");
};

const closeReviewModal = () => {
  showReviewModal.value = false;
  selectedArticle.value = null;
};
</script>
