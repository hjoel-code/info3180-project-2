<script>
export default {
    created() {
        window.sessionStorage.clear()
        window.location.replace('/')
    }
}
</script>