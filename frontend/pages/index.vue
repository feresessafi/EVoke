<template>
  <div class="flex h-screen bg-zinc-50 dark:bg-zinc-950">
    <AppSidebar />
    
    <!-- Main Content -->
    <main class="flex-1 overflow-auto">
      <div class="p-6 space-y-6">
        <!-- Header Section -->
        <div class="flex justify-between items-center">
          <div>
            <h1 class="text-2xl font-bold text-zinc-900 dark:text-zinc-50">Dashboard</h1>
            <p class="text-sm text-zinc-500 dark:text-zinc-400">Manage and generate articles for efahrer.com</p>
          </div>
          <Button class="gap-2">
            <PlusCircle class="h-4 w-4" />
            New Article
          </Button>
        </div>

        <!-- Quick Stats -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <Card>
            <CardHeader class="space-y-1">
              <CardTitle class="text-sm font-medium">Articles in Queue</CardTitle>
              <CardDescription class="text-2xl font-bold">12</CardDescription>
            </CardHeader>
          </Card>
          <Card>
            <CardHeader class="space-y-1">
              <CardTitle class="text-sm font-medium">Published Today</CardTitle>
              <CardDescription class="text-2xl font-bold">8</CardDescription>
            </CardHeader>
          </Card>
          <Card>
            <CardHeader class="space-y-1">
              <CardTitle class="text-sm font-medium">Trending Topics</CardTitle>
              <CardDescription class="text-2xl font-bold">5</CardDescription>
            </CardHeader>
          </Card>
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
            <Card v-for="article in articles" :key="article.id" class="hover:shadow-lg transition-shadow">
              <CardHeader>
                <CardTitle class="line-clamp-2">{{ article.title }}</CardTitle>
                <CardDescription class="flex items-center gap-2">
                  <Badge :variant="article.status === 'draft' ? 'secondary' : 'default'">
                    {{ article.status }}
                  </Badge>
                  <span class="text-xs">{{ article.date }}</span>
                </CardDescription>
              </CardHeader>
              <CardContent>
                <p class="text-sm text-zinc-600 dark:text-zinc-400 line-clamp-2">
                  {{ article.excerpt }}
                </p>
              </CardContent>
              <CardFooter class="flex justify-between">
                <Button variant="ghost" size="sm">
                  <PenSquare class="h-4 w-4 mr-2" />
                  Edit
                </Button>
                <Button variant="ghost" size="sm">
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
</template>

<script setup>
import AppSidebar from '@/components/AppSidebar.vue';
import { Button } from '@/components/ui/button';
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/components/ui/card';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Badge } from '@/components/ui/badge';
import { PlusCircle, PenSquare, Eye } from 'lucide-vue-next';

// Sample data - would come from your store/API
const articles = [
  {
    id: 1,
    title: "Tesla's New Battery Technology Promises 500-Mile Range",
    status: "draft",
    date: "2h ago",
    excerpt: "Revolutionary new battery technology could extend electric vehicle range significantly...",
  },
  {
    id: 2,
    title: "BMW Announces All-Electric SUV Lineup for 2025",
    status: "published",
    date: "5h ago",
    excerpt: "German automaker commits to full electrification of its SUV range...",
  },
  {
    id: 3,
    title: "Solar-Powered Charging Stations: The Future of EV Infrastructure",
    status: "draft",
    date: "1d ago",
    excerpt: "New network of solar-powered charging stations to be deployed across Germany...",
  },
  {
    id: 4,
    title: "Volkswagen ID.4 Sets New Range Record",
    status: "published",
    date: "1d ago",
    excerpt: "Latest tests show impressive range improvements in real-world conditions...",
  },
  {
    id: 5,
    title: "The Rise of Electric Motorcycles in Urban Mobility",
    status: "draft",
    date: "2d ago",
    excerpt: "How electric motorcycles are transforming urban transportation...",
  },
  {
    id: 6,
    title: "Breakthrough in Solid-State Battery Technology",
    status: "published",
    date: "2d ago",
    excerpt: "New research shows promising results for next-generation battery technology...",
  },
];
</script>
