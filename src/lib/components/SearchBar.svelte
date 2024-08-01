<script lang="ts">
	import Search from 'lucide-svelte/icons/search';
	import { Input } from '$lib/components/ui/input/index.js';
</script>

<div class="relative ml-auto flex-1 md:grow-0">
	<Search class="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
	<Input
		type="search"
		placeholder="Search..."
		class="w-full rounded-lg bg-background pl-8 md:w-[200px] lg:w-[400px]"
	/>
</div>
