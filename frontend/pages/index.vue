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

        <!-- Performance Metrics -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
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
                      <span class="text-sm text-muted-foreground">articles in progress</span>
                    </div>
                  </div>
                  <Button variant="outline" size="sm">
                    View
                  </Button>
                </div>

                <!-- Quick Actions -->
                <div class="grid grid-cols-2 gap-4">
                  <div class="space-y-2 p-3 bg-zinc-100 dark:bg-zinc-900 rounded-lg">
                    <div class="flex items-center justify-between">
                      <span class="text-sm font-medium">Ready for Review</span>
                      <Badge>8</Badge>
                    </div>
                    <div class="text-xs text-muted-foreground">
                      Last updated 5m ago
                    </div>
                  </div>
                  <div class="space-y-2 p-3 bg-zinc-100 dark:bg-zinc-900 rounded-lg">
                    <div class="flex items-center justify-between">
                      <span class="text-sm font-medium">Needs Attention</span>
                      <Badge variant="destructive">2</Badge>
                    </div>
                    <div class="text-xs text-muted-foreground">
                      Requires editor input
                    </div>
                  </div>
                </div>

                <!-- Recent Sources -->
                <div class="space-y-2">
                  <div class="flex items-center justify-between">
                    <h4 class="text-sm font-medium">Recent Sources</h4>
                    <Button variant="ghost" size="sm" class="h-8 text-xs">
                      View All
                    </Button>
                  </div>
                  <div class="space-y-2">
                    <div v-for="source in recentSources" :key="source.name" 
                         class="flex items-center justify-between p-2 hover:bg-zinc-100 dark:hover:bg-zinc-900 rounded-md transition-colors">
                      <div class="flex items-center space-x-2">
                        <component :is="source.icon" class="h-4 w-4 text-muted-foreground" />
                        <span class="text-sm">{{ source.name }}</span>
                      </div>
                      <Badge variant="secondary" class="text-xs">{{ source.count }}</Badge>
                    </div>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>

          <!-- Topic Analysis Card -->
          <Card>
            <CardHeader>
              <CardTitle class="text-base font-medium">Trending Topics</CardTitle>
              <CardDescription>Most discussed subjects</CardDescription>
            </CardHeader>
            <CardContent>
              <div class="space-y-4">
                <div v-for="topic in trendingTopics" :key="topic.name" class="flex items-center gap-4">
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
            </CardContent>
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
import { Progress } from '@/components/ui/progress';
import { Badge } from '@/components/ui/badge';
import { PlusCircle, PenSquare, Eye, TrendingUp, TrendingDown, Zap } from 'lucide-vue-next';

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

const trendingTopics = [
  {
    name: "Electric Vehicle Batteries",
    mentions: 342,
    trend: "up",
    percentage: 24
  },
  {
    name: "Charging Infrastructure",
    mentions: 275,
    trend: "up",
    percentage: 18
  },
  {
    name: "Tesla Model Updates",
    mentions: 198,
    trend: "down",
    percentage: 5
  },
  {
    name: "Solid State Technology",
    mentions: 165,
    trend: "up",
    percentage: 12
  }
];
</script>
