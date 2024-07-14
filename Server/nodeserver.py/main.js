const express=require('express');
const app=express();
const multer=require('multer');
const axios=require('axios')
const path=require('path')

const storage = multer.diskStorage({
    destination:(req,file,cb)=>{
        cb(null,'Images')
    },

    filename: (req,file,cb)=>{
        console.log(file);
        cb(null,Date.now()+path.extname(file.originalname))
    }
});

const upload=multer({storage:storage})

const uploadFileClass = async (req, res, model, input) => {
    if (res.statusCode === 401) {
        return res.status(401).json({ error: 'Unauthorized' });
    }
    if (!req.file) {
        return res.status(400).json({ message: 'No file uploaded' });
    }
    try {
        const formData = new FormData();
        formData.append(`${input}`, req.file.buffer, req.file.originalname);
        const flaskResponse = await axios.post(`http://127.0.0.1:5000/${input}`, formData, {
            headers: {
                ...formData.getHeaders()
            },
            responseType: `${input==='video' ? 'stream' : 'arraybuffer'}`
        });
        if(input==='video') flaskResponse.data.pipe(res);
        else {
            res.set('Content-Type', 'image/png'); // Set the response content type to image
            res.send(Buffer.from(flaskResponse.data, 'binary')); // Send the response as binary data
        }
    } catch (error) {
        console.log(error);
        res.status(500).json({ message: 'Error processing video', error: error.message });
    }
};

app.get('/home',(req,res)=>{
    res.send("JI");
})

// app.post('/video',(req,res)=>{

// })


app.post('/image',upload.single('image'),(req,res)=>{
    uploadFileClass(req, res,'image')
});

app.listen(10)