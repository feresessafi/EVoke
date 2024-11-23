<template>
    <DialogContent class="sm:max-w-[900px] max-h-[90vh]">
      <DialogHeader>
        <DialogTitle class="text-xl font-bold flex items-center gap-2">
          {{ article?.story_title }}
          <Badge :variant="getStatusVariant(article?.status)" class="ml-2">
            {{ formatStatus(article?.status) }}
          </Badge>
        </DialogTitle>
        <DialogDescription class="flex items-center gap-4 text-sm text-muted-foreground">
          <span class="flex items-center gap-1">
            <Clock class="h-3 w-3" />
            {{ getTimeAgo(article?.date) }}
          </span>
          <span class="flex items-center gap-1">
            <FileText class="h-3 w-3" />
            {{ article?.article_text.split(' ').length }} words
          </span>
          <span class="flex items-center gap-1">
            <Link class="h-3 w-3" />
            {{ article?.source_count }} sources
          </span>
        </DialogDescription>
      </DialogHeader>
  
      <div class="mt-6 space-y-6">
        <!-- Article Content -->
        <div class="prose dark:prose-invert max-w-none">
          {{ article?.article_text }}
        </div>
  
        <!-- Sources -->
        <div class="space-y-2">
          <h3 class="text-lg font-semibold">Sources</h3>
          <ul class="space-y-2">
            <li v-for="source in article?.sources" :key="source" 
                class="flex items-center gap-2 text-sm text-muted-foreground">
              <Globe class="h-4 w-4" />
              <a :href="source" target="_blank" rel="noopener noreferrer" 
                 class="hover:underline">
                {{ source }}
              </a>
            </li>
          </ul>
        </div>
      </div>
  
      <DialogFooter class="mt-6">
        <Button variant="outline" @click="$emit('close')">
          Cancel
        </Button>
        <Button variant="destructive" @click="handleReject" class="ml-2">
          Needs Revision
        </Button>
        <Button @click="handleApprove" class="ml-2">
          Approve
        </Button>
      </DialogFooter>
    </DialogContent>
  </template>
  
  <script setup lang="ts">
  import { computed } from 'vue';
  import { Clock, FileText, Link, Globe } from 'lucide-vue-next';
  import { Button } from '@/components/ui/button';
  import { Badge } from '@/components/ui/badge';
  import {
    DialogContent,
    DialogHeader,
    DialogFooter,
    DialogTitle,
    DialogDescription,
  } from '@/components/ui/dialog';
  import { getStatusVariant, formatStatus } from '@/utils/status';
  
  const props = defineProps({
    article: {
      type: Object,
      required: true
    }
  });
  
  const emit = defineEmits(['close', 'approve', 'reject']);
  
  const getTimeAgo = (dateString: string) => {
    const date = new Date(dateString);
    const now = new Date();
    const diffInHours = Math.floor((now.getTime() - date.getTime()) / (1000 * 60 * 60));
    
    if (diffInHours < 24) {
      return `${diffInHours}h ago`;
    }
    return `${Math.floor(diffInHours / 24)}d ago`;
  };
  
  const handleApprove = () => {
    emit('approve', props.article);
    emit('close');
  };
  
  const handleReject = () => {
    emit('reject', props.article);
    emit('close');
  };
  </script> 