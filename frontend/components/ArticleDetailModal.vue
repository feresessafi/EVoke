<template>
  <Dialog :open="isOpen" @update:open="closeModal">
    <DialogContent class="sm:max-w-[800px] max-h-[90vh] overflow-auto">
      <DialogHeader>
        <DialogTitle class="text-xl font-semibold">{{ article.story_title }}</DialogTitle>
        <DialogDescription class="flex items-center gap-2 mt-2">
          <Badge :variant="article.status === 'draft' ? 'secondary' : 'default'">
            {{ article.status }}
          </Badge>
          <span class="text-sm text-muted-foreground">{{ article.date }}</span>
        </DialogDescription>
      </DialogHeader>

      <!-- Article Content -->
      <div class="space-y-6">
        <!-- Main Content -->
        <div class="space-y-4">
          <!-- Full Article Text -->
          <div class="prose dark:prose-invert max-w-none">
            <p class="text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed whitespace-pre-wrap">
              {{ article.article_text }}
            </p>
          </div>

          <!-- Article Stats -->
          <div class="grid grid-cols-3 gap-4 py-2">
            <div class="p-3 bg-zinc-100 dark:bg-zinc-900 rounded-lg space-y-1">
              <p class="text-sm text-muted-foreground">Word Count</p>
              <p class="text-lg font-semibold">{{ article.article_text.split(' ').length }}</p>
            </div>
            <div class="p-3 bg-zinc-100 dark:bg-zinc-900 rounded-lg space-y-1">
              <p class="text-sm text-muted-foreground">Sources</p>
              <p class="text-lg font-semibold">{{ article.source_count }}</p>
            </div>
            <div class="p-3 bg-zinc-100 dark:bg-zinc-900 rounded-lg space-y-1">
              <p class="text-sm text-muted-foreground">AI Score</p>
              <p class="text-lg font-semibold text-primary">92%</p>
            </div>
          </div>

          <!-- Source Links -->
          <div class="space-y-2 bg-zinc-50 dark:bg-zinc-900 p-4 rounded-lg">
            <h4 class="text-sm font-medium">Sources Used</h4>
            <div class="space-y-2">
              <div v-for="source in article.sources" :key="source" 
                   class="flex items-center justify-between text-sm p-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 rounded-md transition-colors">
                <div class="flex items-center gap-2">
                  <Globe class="h-4 w-4 text-muted-foreground" />
                  <span class="truncate">{{ source }}</span>
                </div>
                <Button 
                  variant="ghost" 
                  size="sm"
                  @click="handleSourceClick(source)"
                >
                  <ExternalLink class="h-4 w-4" />
                </Button>
              </div>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex justify-end gap-2 pt-4 border-t">
          <Button variant="outline" class="gap-2" @click="closeModal">
            Close
          </Button>
          <Button class="gap-2">
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
import { 
  PenSquare, 
  Globe,
  ExternalLink,
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

// Add this handler function
const handleSourceClick = (sourceUrl) => {
  window.open(sourceUrl, '_blank');
};
</script> 