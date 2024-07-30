<script lang="ts">
	import StarOnGitHub from './StarOnGitHub.svelte';
	import MadeWithLove from './MadeWithLove.svelte';
	import '$src/app.css';
	import { statusBarVisible } from '$lib/stores/ui';
</script>

{#if $statusBarVisible}
	<div class="status-bar fixed bottom-0 left-0 w-full border-t">
		<div class="flex items-center justify-center">
			<MadeWithLove />
			<StarOnGitHub />
		</div>
	</div>
{/if}
