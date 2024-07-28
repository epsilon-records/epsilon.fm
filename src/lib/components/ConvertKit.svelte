<script lang="ts">
	function loadConvertKit(node: HTMLElement) {
		const script = document.createElement('script');
		script.src = 'https://epsilon.ck.page/47e61bac90/index.js';
		script.async = true;
		script.setAttribute('data-uid', '47e61bac90');
		node.appendChild(script);
	}
</script>

<div class="flex items-center justify-center" use:loadConvertKit>
	<!-- ConvertKit form will be inserted here by the script -->
</div>
