# AI-Powered Exam Supervision Monitoring System

## 📋 High-Level Requirements (HLRs)
1. **Real-Time Cheating Detection:** Detect suspicious activities during exams using YOLOv11 models.
2. **Video Processing:** Analyze real-time video feeds to identify unauthorized behaviors.
3. **Multi-Modal Data Integration:** Incorporate audio, facial recognition, and biometric data for robust monitoring.
4. **Supervisor Dashboard:** Provide an intuitive interface for supervisors with real-time alerts and monitoring tools.

## 🔍 Low-Level Requirements (LLRs)
1. **Model Training:**
   - Use data augmentation techniques (grayscale, blurring, noise addition).
   - Achieve over 90% detection accuracy with 50+ training epochs.
2. **Video Analysis:**
   - Implement efficient video streaming using TensorFlow and OpenCV.
   - Process high-resolution video with minimal latency.
3. **Alert System:**
   - Dynamic logging of suspicious activities.
   - Real-time notifications for supervisors.
4. **User Interface:**
   - Display multiple video streams simultaneously.
   - Highlight flagged incidents with timestamps for easy review.

## ⚙️ Non-Functional Requirements (NFRs)
1. **Performance:** Ensure detection accuracy >90% with real-time processing capability.
2. **Scalability:** Support both small-scale classroom exams and large remote proctoring setups.
3. **Reliability:** Provide consistent monitoring without system crashes or false alerts.
4. **Usability:** Develop an easy-to-navigate interface for non-technical users (exam supervisors).
5. **Security:** Ensure secure handling of video feeds and student data.

## 📊 Summary of Requirements
The **AI-Powered Exam Supervision Monitoring System** aims to enhance academic integrity through real-time video analysis and cheating detection. By leveraging advanced AI models like YOLOv11, integrating multi-modal data, and offering an intuitive dashboard, the system ensures efficient, reliable, and scalable exam monitoring for both in-person and remote environments.

---

> 📅 **Project Supervisor:** Sanhita Manna  
> 🤖 **Cluster:** AI/ML (Group: CS15)  
> 🎯 **Conferences Targeted:** IEEE CAI 2025, IEEE ICAIE 2023

