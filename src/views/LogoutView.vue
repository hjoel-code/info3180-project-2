<script>
export default {
    created() {
        window.localStorage.clear()
        window.location.replace('/')
    }
}
</script>