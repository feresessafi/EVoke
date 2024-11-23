<template>
  <Dialog :open="isOpen" @update:open="closeModal">
    <DialogContent class="sm:max-w-[1000px] max-h-[90vh] overflow-auto">
      <DialogHeader>
        <DialogTitle class="text-2xl font-semibold">{{ article.story_title }}</DialogTitle>
        <DialogDescription class="flex items-center gap-2 mt-2">
          <Badge :variant="article.status === 'draft' ? 'secondary' : 'default'">
            {{ article.status }}
          </Badge>
          <span class="text-sm text-muted-foreground">{{ article.date }}</span>
        </DialogDescription>
      </DialogHeader>

      <!-- Article Content -->
      <div class="flex gap-6 mt-4">
        <!-- Main Content Column -->
        <div class="flex-1 space-y-6">
          <!-- Media Placeholder -->
          <div class="relative aspect-video w-full overflow-hidden rounded-lg">
            <Skeleton class="absolute inset-0" />
            <div class="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent" />
          </div>

          <!-- Article Text -->
          <div class="prose dark:prose-invert max-w-none">
            <p class="text-base leading-relaxed whitespace-pre-wrap text-zinc-800 dark:text-zinc-200">
              {{ article.article_text }}
            </p>
          </div>
        </div>

        <!-- Metadata Sidebar -->
        <div class="w-64 space-y-6">
          <!-- Article Stats -->
          <div class="space-y-4">
            <div class="p-4 bg-zinc-100 dark:bg-zinc-900 rounded-lg space-y-2">
              <div class="space-y-1">
                <p class="text-sm text-muted-foreground">AI Score</p>
                <div class="flex items-center justify-between">
                  <p class="text-lg font-semibold text-primary">92%</p>
                  <Sparkles class="h-4 w-4 text-primary" />
                </div>
              </div>
              <Progress value={92} class="h-1" />
            </div>

            <div class="p-4 bg-zinc-100 dark:bg-zinc-900 rounded-lg space-y-3">
              <div class="space-y-1">
                <p class="text-sm text-muted-foreground">Word Count</p>
                <p class="text-base font-medium">{{ article.article_text.split(' ').length }}</p>
              </div>
              <div class="space-y-1">
                <p class="text-sm text-muted-foreground">Sources</p>
                <p class="text-base font-medium">{{ article.source_count }}</p>
              </div>
              <div class="space-y-1">
                <p class="text-sm text-muted-foreground">Reading Time</p>
                <p class="text-base font-medium">{{ Math.ceil(article.article_text.split(' ').length / 200) }} min</p>
              </div>
            </div>

            <!-- Sources List -->
            <div class="space-y-2">
              <h3 class="text-sm font-medium">Sources</h3>
              <div class="space-y-2">
                <Button 
                  v-for="(source, index) in article.sources" 
                  :key="index"
                  variant="outline"
                  class="w-full justify-start text-sm"
                  @click="handleSourceClick(source)"
                >
                  <Globe class="h-3 w-3 mr-2" />
                  Source {{ index + 1 }}
                  <ExternalLink class="h-3 w-3 ml-auto" />
                </Button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex justify-between items-center gap-2 pt-6 mt-6 border-t">
        <Button variant="destructive" size="sm" @click="$emit('delete')">
          Delete Article
        </Button>
        <div class="flex gap-2">
          <Button variant="outline" size="sm" @click="closeModal">
            Close
          </Button>
          <Button size="sm" class="gap-2">
            <PenSquare class="h-4 w-4" />
            Edit Article
          </Button>
        </div>
      </div>
    </DialogContent>
  </Dialog>
</template>

<script setup>
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription } from '@/components/ui/dialog';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Progress } from '@/components/ui/progress';
import { Skeleton } from '@/components/ui/skeleton';
import { 
  PenSquare, 
  Globe,
  ExternalLink,
  Sparkles,
} from 'lucide-vue-next';

const props = defineProps({
  isOpen: Boolean,
  article: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['close', 'update', 'delete']);

const closeModal = () => {
  emit('close');
};

const handleSourceClick = (sourceUrl) => {
  window.open(sourceUrl, '_blank');
};
</script>

<style scoped>
.prose {
  max-width: none;
}
</style> 