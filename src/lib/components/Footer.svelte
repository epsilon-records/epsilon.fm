<script lang="ts">
	import StarOnGitHub from './StarOnGitHub.svelte';
	import MadeWithLove from './MadeWithLove.svelte';
	import '$src/app.css';
</script>

<footer class="fixed bottom-0 left-0 w-full border-t">
	<div class="flex items-center justify-center">
		<MadeWithLove />
		<StarOnGitHub />
	</div>
</footer>
