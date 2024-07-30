<script lang="ts">
	import StarOnGitHub from './StarOnGitHub.svelte';
	import MadeWithLove from './MadeWithLove.svelte';
	import '$src/app.css';
</script>

<footer class="fixed bottom-0 left-0 w-full bg-gray-100 py-2 text-center">
	<slot name="footer">
		<MadeWithLove></MadeWithLove>
		<StarOnGitHub></StarOnGitHub>
	</slot>
</footer>
